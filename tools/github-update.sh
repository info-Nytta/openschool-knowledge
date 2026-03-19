#!/bin/bash
# GitHub Classroom template repók frissítése egy Organization-ben.
#
# Használat:
#   ./github-update.sh <ORGANIZATION> <TEMPLATE_MAPPA> [--classroom]
#
# Példa:
#   ./github-update.sh OpenSchool-HU ../courses/python-alapok/github-classroom
#   ./github-update.sh OpenSchool-HU ../courses/python-alapok/github-classroom --classroom
#
# Előfeltételek:
#   - GitHub CLI (gh) telepítve és bejelentkezve: https://cli.github.com
#   - Az Organization már létezik a GitHubon
#   - A repók már létre lettek hozva a github-setup.sh szkripttel
#
# Mit csinál:
#   1. Végigmegy a template mappa almappáin (het00-..., het01-..., stb.)
#   2. Meglévő repókat klónozza, tartalmát lecseréli a helyi fájlokra
#   3. Ha van változás, commitolja és pusholja
#
# --classroom mód:
#   A GitHub Classroom saját nevű template repókat hoz létre (pl.
#   python-alapok-git-alapok-het00-git-alapok). A --classroom kapcsolóval
#   a szkript a mappa neve alapján megkeresi a hozzá tartozó repót az
#   Organization-ben (a repo nevének végződése alapján).

set -euo pipefail

# --- Paraméterek ---
CLASSROOM_MODE=false

if [[ $# -lt 2 ]]; then
    echo "Használat: $0 <ORGANIZATION> <TEMPLATE_MAPPA> [--classroom]"
    echo ""
    echo "Példa:"
    echo "  $0 OpenSchool-HU ../courses/python-alapok/github-classroom"
    echo "  $0 OpenSchool-HU ../courses/python-alapok/github-classroom --classroom"
    exit 1
fi

ORG="$1"
TEMPLATE_DIR="$2"

if [[ "${3:-}" == "--classroom" ]]; then
    CLASSROOM_MODE=true
fi

if [[ ! -d "$TEMPLATE_DIR" ]]; then
    echo "HIBA: A mappa nem létezik: $TEMPLATE_DIR"
    exit 1
fi

# --- Ellenőrzés: gh CLI elérhető ---
if ! command -v gh &> /dev/null; then
    echo "HIBA: A 'gh' (GitHub CLI) nincs telepítve."
    echo "Telepítés: https://cli.github.com"
    exit 1
fi

# --- Ellenőrzés: bejelentkezve ---
if ! gh auth status &> /dev/null; then
    echo "HIBA: Nem vagy bejelentkezve. Futtasd: gh auth login"
    exit 1
fi

echo "=== GitHub Classroom template update ==="
echo "Organization: $ORG"
echo "Template mappa: $TEMPLATE_DIR"
if [[ "$CLASSROOM_MODE" == true ]]; then
    echo "Mód: --classroom (repo keresés név végződés alapján)"
fi
echo ""

# --- Classroom mód: repólista lekérése ---
if [[ "$CLASSROOM_MODE" == true ]]; then
    echo "Repólista lekérése..."
    REPO_LIST=$(gh repo list "$ORG" --limit 500 --json name --jq '.[].name')
    echo ""
fi

# --- Repók frissítése ---
UPDATED=0
SKIPPED=0
FAILED=0
UNCHANGED=0

for dir in "$TEMPLATE_DIR"/*/; do
    REPO_NAME=$(basename "$dir")

    # Vizsgák és üres mappák kihagyása
    if [[ ! -f "$dir/README.md" ]]; then
        echo "SKIP: $REPO_NAME (nincs README.md)"
        SKIPPED=$((SKIPPED + 1))
        continue
    fi

    echo "--- $REPO_NAME ---"

    # Repo neve meghatározása
    if [[ "$CLASSROOM_MODE" == true ]]; then
        # Classroom mód: keresés a repólistában név végződés alapján
        REMOTE_REPO=$(echo "$REPO_LIST" | grep -E ".*-${REPO_NAME}$" | head -1)
        if [[ -z "$REMOTE_REPO" ]]; then
            echo "  Nem található Classroom repo (-${REPO_NAME} végződéssel), kihagyva."
            SKIPPED=$((SKIPPED + 1))
            continue
        fi
        echo "  Classroom repo: $REMOTE_REPO"
    else
        REMOTE_REPO="$REPO_NAME"
    fi

    # Ellenőrzés: létezik-e a repo
    if ! gh repo view "$ORG/$REMOTE_REPO" &> /dev/null; then
        echo "  Nem létezik, kihagyva. (Hozd létre először: github-setup.sh)"
        SKIPPED=$((SKIPPED + 1))
        continue
    fi

    # Repo klónozása
    TEMP_DIR=$(mktemp -d)
    if ! gh repo clone "$ORG/$REMOTE_REPO" "$TEMP_DIR" -- -q 2>/dev/null; then
        echo "  HIBA: Klónozás sikertelen."
        FAILED=$((FAILED + 1))
        rm -rf "$TEMP_DIR"
        continue
    fi

    # Meglévő fájlok törlése (a .git mappa kivételével)
    find "$TEMP_DIR" -mindepth 1 -maxdepth 1 ! -name '.git' -exec rm -rf {} +

    # Új fájlok másolása
    cp -r "$dir"/* "$TEMP_DIR"/
    cp -r "$dir"/.github "$TEMP_DIR"/ 2>/dev/null || true

    # Változások commitolása és pusholása
    pushd "$TEMP_DIR" > /dev/null
    git add -A

    if git diff --cached --quiet; then
        echo "  Nincs változás."
        UNCHANGED=$((UNCHANGED + 1))
    else
        git commit -q -m "update template"
        if git push -q; then
            echo "  Frissítve. ✅"
            UPDATED=$((UPDATED + 1))
        else
            echo "  HIBA: Push sikertelen."
            FAILED=$((FAILED + 1))
        fi
    fi

    popd > /dev/null
    rm -rf "$TEMP_DIR"

    echo ""
done

echo "=== Összegzés ==="
echo "Frissítve:      $UPDATED"
echo "Nincs változás:  $UNCHANGED"
echo "Kihagyva:        $SKIPPED"
echo "Hibás:           $FAILED"
