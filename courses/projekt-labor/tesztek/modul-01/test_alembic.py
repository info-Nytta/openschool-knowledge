"""
Modul 1 — Projekt indítás: Alembic konfiguráció verifikáció.
Ellenőrzi, hogy az Alembic migrációs keretrendszer be van állítva.
"""

from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent


def test_alembic_ini_exists():
    """Az alembic.ini létezik a backend mappában."""
    assert (REPO_ROOT / "backend" / "alembic.ini").is_file(), (
        "Hiányzik a backend/alembic.ini. Futtasd: cd backend && alembic init alembic"
    )


def test_alembic_env_py_exists():
    """Az alembic/env.py létezik."""
    assert (REPO_ROOT / "backend" / "alembic" / "env.py").is_file(), (
        "Hiányzik a backend/alembic/env.py."
    )


def test_alembic_versions_dir_exists():
    """Az alembic/versions/ mappa létezik."""
    assert (REPO_ROOT / "backend" / "alembic" / "versions").is_dir(), (
        "Hiányzik a backend/alembic/versions/ mappa."
    )


def test_ci_workflow_exists():
    """A GitHub Actions CI workflow létezik."""
    ci_path = REPO_ROOT / ".github" / "workflows" / "ci.yml"
    ci_path_yaml = REPO_ROOT / ".github" / "workflows" / "ci.yaml"
    assert ci_path.is_file() or ci_path_yaml.is_file(), (
        "Hiányzik a .github/workflows/ci.yml (vagy ci.yaml). "
        "Hozd létre a CI pipeline-t."
    )


def test_precommit_config_exists():
    """A pre-commit konfiguráció létezik."""
    assert (REPO_ROOT / ".pre-commit-config.yaml").is_file(), (
        "Hiányzik a .pre-commit-config.yaml. "
        "Állítsd be a ruff linter-t pre-commit hook-ként."
    )


def test_database_py_exists():
    """A backend/app/database.py létezik."""
    assert (REPO_ROOT / "backend" / "app" / "database.py").is_file(), (
        "Hiányzik a backend/app/database.py. "
        "Ez tartalmazza a SQLAlchemy engine és session konfigurációt."
    )


def test_config_py_exists():
    """A backend/app/config.py létezik."""
    assert (REPO_ROOT / "backend" / "app" / "config.py").is_file(), (
        "Hiányzik a backend/app/config.py. "
        "Ez tartalmazza a Settings osztályt (pydantic-settings)."
    )


def test_conftest_exists():
    """A backend/tests/conftest.py létezik."""
    assert (REPO_ROOT / "backend" / "tests" / "conftest.py").is_file(), (
        "Hiányzik a backend/tests/conftest.py. "
        "Ez tartalmazza a teszt adatbázis konfigurációt."
    )
