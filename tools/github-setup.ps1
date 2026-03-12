# GitHub Classroom template repók automatikus létrehozása egy Organization-ben.
#
# Használat:
#   .\github-setup.ps1 <ORGANIZATION> <TEMPLATE_MAPPA>
#
# Példa:
#   .\github-setup.ps1 openschool-python-2026 ..\..\courses\python-alapok\github-classroom
#
# Előfeltételek:
#   - GitHub CLI (gh) telepítve és bejelentkezve: https://cli.github.com
#   - Az Organization már létezik a GitHubon
#
# Mit csinál:
#   1. Végigmegy a template mappa almappáin (het00-..., het01-..., stb.)
#   2. Minden almappából GitHub repót hoz létre az Organization alatt
#   3. Feltölti a fájlokat
#   4. Template repository-nak jelöli a repót

param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$Organization,

    [Parameter(Mandatory=$true, Position=1)]
    [string]$TemplateDir
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

Write-Host "=== GitHub Classroom template setup ==="
Write-Host "Organization: $Organization"
Write-Host "Template mappa: $TemplateDir"
Write-Host ""

# --- Repók létrehozása ---
$Created = 0
$Skipped = 0
$Failed = 0

foreach ($dir in Get-ChildItem -Path $TemplateDir -Directory | Sort-Object Name) {
    $RepoName = $dir.Name

    # Vizsgák és üres mappák kihagyása
    if (-not (Test-Path (Join-Path $dir.FullName "README.md"))) {
        Write-Host "SKIP: $RepoName (nincs README.md)"
        $Skipped++
        continue
    }

    Write-Host "--- $RepoName ---"

    # Ellenőrzés: létezik-e már a repo
    $null = gh repo view "$Organization/$RepoName" 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  Mar letezik, kihagyva."
        $Skipped++
        continue
    }

    # Repo létrehozása (privát, üres)
    gh repo create "$Organization/$RepoName" --private --description "GitHub Classroom template: $RepoName"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  HIBA: Nem sikerult letrehozni a repot."
        $Failed++
        continue
    }

    # Fájlok feltöltése
    $TempDir = Join-Path ([System.IO.Path]::GetTempPath()) ([System.Guid]::NewGuid().ToString())
    New-Item -ItemType Directory -Path $TempDir | Out-Null

    Copy-Item -Path (Join-Path $dir.FullName "*") -Destination $TempDir -Recurse -Force
    $githubDir = Join-Path $dir.FullName ".github"
    if (Test-Path $githubDir) {
        Copy-Item -Path $githubDir -Destination $TempDir -Recurse -Force
    }

    Push-Location $TempDir
    git init -q
    git add .
    git commit -q -m "template"
    git branch -M main
    git remote add origin "https://github.com/$Organization/$RepoName.git"
    $pushResult = git push -u origin main -q 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  Feltoltve."
    } else {
        Write-Host "  HIBA: Push sikertelen."
        $Failed++
        Pop-Location
        Remove-Item -Path $TempDir -Recurse -Force
        continue
    }
    Pop-Location
    Remove-Item -Path $TempDir -Recurse -Force

    # Template repository beállítás (GitHub API)
    $null = gh api -X PATCH "repos/$Organization/$RepoName" -f is_template=true 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  Template repository: ✅"
    } else {
        Write-Host "  FIGYELEM: Template jeloles sikertelen (kezzel allitsd be)."
    }

    $Created++
    Write-Host ""
}

Write-Host "=== Osszegzes ==="
Write-Host "Letrehozva: $Created"
Write-Host "Kihagyva:   $Skipped"
Write-Host "Hiba:       $Failed"
