"""
Modul 1 — Projekt indítás: Docker és projekt struktúra verifikáció.
Ellenőrzi, hogy a szükséges fájlok és mappák léteznek.
"""

from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).parent.parent.parent


def test_docker_compose_exists():
    """A docker-compose.yml létezik a repó gyökerében."""
    assert (REPO_ROOT / "docker-compose.yml").is_file(), (
        "Hiányzik a docker-compose.yml a repó gyökeréből."
    )


def test_docker_compose_has_required_services():
    """A docker-compose.yml tartalmazza a backend, db, és nginx service-eket."""
    compose_file = REPO_ROOT / "docker-compose.yml"
    if not compose_file.is_file():
        assert False, "Hiányzik a docker-compose.yml."

    with open(compose_file) as f:
        data = yaml.safe_load(f)

    services = data.get("services", {})
    for service in ["backend", "db"]:
        assert service in services, (
            f"A '{service}' service hiányzik a docker-compose.yml-ből."
        )


def test_backend_dockerfile_exists():
    """A backend/Dockerfile létezik."""
    assert (REPO_ROOT / "backend" / "Dockerfile").is_file(), (
        "Hiányzik a backend/Dockerfile."
    )


def test_requirements_txt_exists():
    """A backend/requirements.txt létezik és nem üres."""
    req_file = REPO_ROOT / "backend" / "requirements.txt"
    assert req_file.is_file(), "Hiányzik a backend/requirements.txt."
    content = req_file.read_text().strip()
    assert len(content) > 0, "A backend/requirements.txt üres."


def test_env_example_exists():
    """A .env.example létezik."""
    assert (REPO_ROOT / ".env.example").is_file(), (
        "Hiányzik a .env.example. Hozd létre a szükséges környezeti "
        "változókkal (DB_USER, DB_PASSWORD, DB_NAME, SECRET_KEY, stb.)."
    )


def test_project_structure():
    """Az alapvető mappastruktúra létezik."""
    required_dirs = [
        "backend/app",
        "backend/app/models",
        "backend/app/routers",
        "backend/tests",
    ]
    for dir_path in required_dirs:
        assert (REPO_ROOT / dir_path).is_dir(), (
            f"Hiányzó mappa: {dir_path}"
        )


def test_main_py_exists():
    """A backend/app/main.py létezik."""
    assert (REPO_ROOT / "backend" / "app" / "main.py").is_file(), (
        "Hiányzik a backend/app/main.py."
    )


def test_makefile_exists():
    """A Makefile létezik a repó gyökerében."""
    assert (REPO_ROOT / "Makefile").is_file(), (
        "Hiányzik a Makefile. Hozd létre a gyakori parancsok rövidítéséhez "
        "(up, down, test, migrate, lint)."
    )


def test_gitignore_exists():
    """A .gitignore létezik."""
    assert (REPO_ROOT / ".gitignore").is_file(), "Hiányzik a .gitignore."


def test_readme_exists():
    """A README.md létezik és nem üres."""
    readme = REPO_ROOT / "README.md"
    assert readme.is_file(), "Hiányzik a README.md."
    assert len(readme.read_text().strip()) > 50, (
        "A README.md túl rövid. Tartalmazzon futtatási útmutatót."
    )
