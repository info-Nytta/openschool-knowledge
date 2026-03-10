"""
Modul 5 — Frontend: Oldal struktúra és build verifikáció.
Ellenőrzi, hogy a frontend projekt felépítése helyes.
"""

from pathlib import Path
import json

REPO_ROOT = Path(__file__).parent.parent.parent


def test_frontend_dir_exists():
    """A frontend/ mappa létezik."""
    assert (REPO_ROOT / "frontend").is_dir(), (
        "Hiányzik a frontend/ mappa. Hozd létre az Astro projektet."
    )


def test_package_json_exists():
    """A frontend/package.json létezik."""
    pkg = REPO_ROOT / "frontend" / "package.json"
    assert pkg.is_file(), "Hiányzik a frontend/package.json."


def test_package_json_has_astro():
    """Az Astro dependency szerepel a package.json-ben."""
    pkg = REPO_ROOT / "frontend" / "package.json"
    if not pkg.is_file():
        assert False, "Hiányzik a frontend/package.json."

    data = json.loads(pkg.read_text())
    all_deps = {
        **data.get("dependencies", {}),
        **data.get("devDependencies", {}),
    }
    assert "astro" in all_deps, (
        "Az 'astro' csomag nem szerepel a frontend/package.json dependency-k között."
    )


def test_astro_config_exists():
    """Az Astro konfiguráció létezik."""
    config_paths = [
        REPO_ROOT / "frontend" / "astro.config.mjs",
        REPO_ROOT / "frontend" / "astro.config.ts",
        REPO_ROOT / "frontend" / "astro.config.js",
    ]
    assert any(p.is_file() for p in config_paths), (
        "Hiányzik az astro.config.mjs (vagy .ts/.js)."
    )


def test_pages_directory_exists():
    """A frontend/src/pages/ mappa létezik."""
    pages_dir = REPO_ROOT / "frontend" / "src" / "pages"
    assert pages_dir.is_dir(), "Hiányzik a frontend/src/pages/ mappa."


def test_index_page_exists():
    """A landing page (index) létezik."""
    pages_dir = REPO_ROOT / "frontend" / "src" / "pages"
    index_files = list(pages_dir.glob("index.*"))
    assert len(index_files) > 0, (
        "Hiányzik a frontend/src/pages/index.astro (landing page)."
    )


def test_layout_exists():
    """Legalább egy layout fájl létezik."""
    layouts_dir = REPO_ROOT / "frontend" / "src" / "layouts"
    if layouts_dir.is_dir():
        layouts = list(layouts_dir.glob("*.*"))
        assert len(layouts) > 0, "A layouts/ mappa üres."
    else:
        assert False, "Hiányzik a frontend/src/layouts/ mappa."


def test_frontend_dockerfile_exists():
    """A frontend/Dockerfile létezik."""
    assert (REPO_ROOT / "frontend" / "Dockerfile").is_file(), (
        "Hiányzik a frontend/Dockerfile. "
        "Hozd létre a multi-stage Docker build-et (Node → nginx)."
    )


def test_components_directory_exists():
    """A frontend/src/components/ mappa létezik."""
    components_dir = REPO_ROOT / "frontend" / "src" / "components"
    assert components_dir.is_dir(), (
        "Hiányzik a frontend/src/components/ mappa."
    )
