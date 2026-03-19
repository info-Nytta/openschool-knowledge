# GitHub Classroom template repók frissítése egy Organization-ben.
#
# Használat:
#   .\github-update.ps1 <ORGANIZATION> <TEMPLATE_MAPPA> [-Classroom]
#
# Példa:
#   .\github-update.ps1 OpenSchool-HU ..\courses\python-alapok\github-classroom
#   .\github-update.ps1 OpenSchool-HU ..\courses\python-alapok\github-classroom -Classroom
#
# Előfeltételek:
#   - GitHub CLI (gh) telepítve és bejelentkezve: https://cli.github.com
#   - Az Organization már létezik a GitHubon
#   - A repók már létre lettek hozva a github-setup.ps1 szkripttel
#
# Mit csinál:
#   1. Végigmegy a template mappa almappáin (het00-..., het01-..., stb.)
#   2. Meglévő repókat klónozza, tartalmát lecseréli a helyi fájlokra
#   3. Ha van változás, commitolja és pusholja
#
# -Classroom mód:
#   A GitHub Classroom saját nevű template repókat hoz létre (pl.
#   python-alapok-git-alapok-het00-git-alapok). A -Classroom kapcsolóval
#   a szkript a mappa neve alapján megkeresi a hozzá tartozó repót az
#   Organization-ben (a repo nevének végződése alapján).

param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$Organization,

    [Parameter(Mandatory=$true, Position=1)]
    [string]$TemplateDir,

    [switch]$Classroom
)

$ErrorActionPreference = "Stop"

# --- Ellenőrzés: mappa létezik ---
if (-not (Test-Path $TemplateDir -PathType Container)) {
    Write-Error "HIBA: A mappa nem létezik: $TemplateDir"
    exit 1
}

# --- Ellenőrzés: gh CLI elérhető ---
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Error "HIBA: A 'gh' (GitHub CLI) nincs telepítve. Telepítés: https://cli.github.com"
    exit 1
}

# --- Ellenőrzés: bejelentkezve ---
$null = gh auth status 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Error "HIBA: Nem vagy bejelentkezve. Futtasd: gh auth login"
    exit 1
}

Write-Host "=== GitHub Classroom template update ==="
Write-Host "Organization: $Organization"
Write-Host "Template mappa: $TemplateDir"
if ($Classroom) {
    Write-Host "Mod: -Classroom (repo kereses nev vegzodes alapjan)"
}
Write-Host ""

# --- Classroom mód: repólista lekérése ---
$RepoList = @()
if ($Classroom) {
    Write-Host "Repolista lekerese..."
    $RepoList = (gh repo list $Organization --limit 500 --json name --jq '.[].name') -split "`n"
    Write-Host ""
}

# --- Repók frissítése ---
$Updated = 0
$Skipped = 0
$Failed = 0
$Unchanged = 0

foreach ($dir in Get-ChildItem -Path $TemplateDir -Directory | Sort-Object Name) {
    $RepoName = $dir.Name

    # Vizsgák és üres mappák kihagyása
    if (-not (Test-Path (Join-Path $dir.FullName "README.md"))) {
        Write-Host "SKIP: $RepoName (nincs README.md)"
        $Skipped++
        continue
    }

    Write-Host "--- $RepoName ---"

    # Repo neve meghatározása
    if ($Classroom) {
        $RemoteRepo = $RepoList | Where-Object { $_ -match ".*-${RepoName}$" } | Select-Object -First 1
        if (-not $RemoteRepo) {
            Write-Host "  Nem talalhato Classroom repo (-${RepoName} vegzodessel), kihagyva."
            $Skipped++
            continue
        }
        Write-Host "  Classroom repo: $RemoteRepo"
    } else {
        $RemoteRepo = $RepoName
    }

    # Ellenőrzés: létezik-e a repo
    $null = gh repo view "$Organization/$RemoteRepo" 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  Nem letezik, kihagyva. (Hozd letre eloszor: github-setup.ps1)"
        $Skipped++
        continue
    }

    # Repo klónozása
    $TempDir = Join-Path ([System.IO.Path]::GetTempPath()) ([System.Guid]::NewGuid().ToString())
    gh repo clone "$Organization/$RemoteRepo" $TempDir -- -q 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  HIBA: Klonozas sikertelen."
        $Failed++
        if (Test-Path $TempDir) { Remove-Item -Path $TempDir -Recurse -Force }
        continue
    }

    # Meglévő fájlok törlése (a .git mappa kivételével)
    Get-ChildItem -Path $TempDir -Force | Where-Object { $_.Name -ne '.git' } | Remove-Item -Recurse -Force

    # Új fájlok másolása
    Copy-Item -Path (Join-Path $dir.FullName "*") -Destination $TempDir -Recurse -Force
    $githubDir = Join-Path $dir.FullName ".github"
    if (Test-Path $githubDir) {
        Copy-Item -Path $githubDir -Destination $TempDir -Recurse -Force
    }

    # Változások commitolása és pusholása
    Push-Location $TempDir
    git add -A

    $diffOutput = git diff --cached --quiet 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  Nincs valtozas."
        $Unchanged++
    } else {
        git commit -q -m "update template"
        git push -q 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "  Frissitve. ✅"
            $Updated++
        } else {
            Write-Host "  HIBA: Push sikertelen."
            $Failed++
        }
    }

    Pop-Location
    Remove-Item -Path $TempDir -Recurse -Force

    Write-Host ""
}

Write-Host "=== Osszegzes ==="
Write-Host "Frissitve:      $Updated"
Write-Host "Nincs valtozas:  $Unchanged"
Write-Host "Kihagyva:        $Skipped"
Write-Host "Hiba:            $Failed"
