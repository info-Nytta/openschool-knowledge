#!/bin/bash
# GitHub Classroom template repók automatikus létrehozása egy Organization-ben.
#
# Használat:
#   ./github-setup.sh <ORGANIZATION> <TEMPLATE_MAPPA>
#
# Példa:
#   ./github-setup.sh openschool-python-2026 ../../courses/python-alapok/github-classroom
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

set -euo pipefail

# --- Paraméterek ---
if [[ $# -lt 2 ]]; then
    echo "Használat: $0 <ORGANIZATION> <TEMPLATE_MAPPA>"
    echo ""
    echo "Példa:"
    echo "  $0 openschool-python-2026 ../../courses/python-alapok/github-classroom"
    exit 1
fi

ORG="$1"
TEMPLATE_DIR="$2"

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

echo "=== GitHub Classroom template setup ==="
echo "Organization: $ORG"
echo "Template mappa: $TEMPLATE_DIR"
echo ""

# --- Repók létrehozása ---
CREATED=0
SKIPPED=0
FAILED=0

for dir in "$TEMPLATE_DIR"/*/; do
    # Mappa neve = repo neve
    REPO_NAME=$(basename "$dir")

    # Vizsgák és üres mappák kihagyása
    if [[ ! -f "$dir/README.md" ]]; then
        echo "SKIP: $REPO_NAME (nincs README.md)"
        SKIPPED=$((SKIPPED + 1))
        continue
    fi

    echo "--- $REPO_NAME ---"

    # Ellenőrzés: létezik-e már a repo
    if gh repo view "$ORG/$REPO_NAME" &> /dev/null; then
        echo "  Már létezik, kihagyva."
        SKIPPED=$((SKIPPED + 1))
        continue
    fi

    # Repo létrehozása (privát, üres)
    if ! gh repo create "$ORG/$REPO_NAME" --private --description "GitHub Classroom template: $REPO_NAME"; then
        echo "  HIBA: Nem sikerült létrehozni a repót."
        FAILED=$((FAILED + 1))
        continue
    fi

    # Fájlok feltöltése
    TEMP_DIR=$(mktemp -d)
    cp -r "$dir"/* "$TEMP_DIR"/
    cp -r "$dir"/.github "$TEMP_DIR"/ 2>/dev/null || true

    pushd "$TEMP_DIR" > /dev/null
    git init -q
    git add .
    git commit -q -m "template"
    git branch -M main
    git remote add origin "https://github.com/$ORG/$REPO_NAME.git"
    if git push -u origin main -q; then
        echo "  Feltöltve."
    else
        echo "  HIBA: Push sikertelen."
        FAILED=$((FAILED + 1))
        popd > /dev/null
        rm -rf "$TEMP_DIR"
        continue
    fi
    popd > /dev/null
    rm -rf "$TEMP_DIR"

    # Template repository beállítás (GitHub API)
    if gh api -X PATCH "repos/$ORG/$REPO_NAME" -f is_template=true > /dev/null 2>&1; then
        echo "  Template repository: ✅"
    else
        echo "  FIGYELEM: Template jelölés sikertelen (kézzel állítsd be)."
    fi

    CREATED=$((CREATED + 1))
    echo ""
done

echo "=== Összegzés ==="
echo "Létrehozva: $CREATED"
echo "Kihagyva:   $SKIPPED"
echo "Hibás:      $FAILED"
