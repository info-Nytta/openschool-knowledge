"""
DevSchool Projekt Labor — Verifikációs tesztek
Közös fixture-ök és konfigurációs beállítások.

Használat:
  1. Másold a tesztek/ mappát a devschool-platform repó gyökerébe
  2. cd devschool-platform
  3. pip install -r backend/requirements.txt
  4. pytest tesztek/modul-01/ -v
"""

import os
import pytest
from pathlib import Path

# A devschool-platform repó gyökere (a tesztek/ mappa szülője)
REPO_ROOT = Path(__file__).parent.parent


@pytest.fixture
def repo_root():
    """A devschool-platform repó gyökérmappája."""
    return REPO_ROOT


@pytest.fixture
def backend_dir(repo_root):
    """A backend/ mappa útvonala."""
    return repo_root / "backend"


@pytest.fixture
def frontend_dir(repo_root):
    """A frontend/ mappa útvonala."""
    return repo_root / "frontend"


def file_exists(path: Path) -> bool:
    """Segédfüggvény: létezik-e a fájl."""
    return path.is_file()


def dir_exists(path: Path) -> bool:
    """Segédfüggvény: létezik-e a mappa."""
    return path.is_dir()
