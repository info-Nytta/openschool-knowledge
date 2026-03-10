"""
Modul 3 — Kurzusok és haladás: Dashboard és GitHub API verifikáció.
Ellenőrzi, hogy a haladáskövetés és dashboard endpoint-ok léteznek.
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent


def _setup_backend():
    backend_path = REPO_ROOT / "backend"
    if str(backend_path) not in sys.path:
        sys.path.insert(0, str(backend_path))


def _get_client():
    _setup_backend()
    from app.main import app
    from fastapi.testclient import TestClient
    return TestClient(app)


def test_dashboard_endpoint_requires_auth():
    """A GET /api/me/dashboard endpoint autentikációt igényel."""
    client = _get_client()
    response = client.get("/api/me/dashboard")
    assert response.status_code in (401, 403), (
        f"A /api/me/dashboard endpoint token nélkül "
        f"{response.status_code}-et adott vissza. Elvárt: 401 vagy 403."
    )


def test_my_courses_endpoint_requires_auth():
    """A GET /api/me/courses endpoint autentikációt igényel."""
    client = _get_client()
    response = client.get("/api/me/courses")
    assert response.status_code in (401, 403), (
        f"A /api/me/courses endpoint token nélkül "
        f"{response.status_code}-et adott vissza. Elvárt: 401 vagy 403."
    )


def test_github_service_exists():
    """A GitHub API service modul létezik."""
    _setup_backend()
    try:
        from app.services.github import check_exercise_status
        assert callable(check_exercise_status)
    except ImportError:
        assert False, (
            "Nem sikerült importálni: from app.services.github import check_exercise_status. "
            "Hozd létre a GitHub API szolgáltatást."
        )


def test_progress_service_exists():
    """A progress service modul létezik."""
    _setup_backend()
    progress_path = REPO_ROOT / "backend" / "app" / "services"
    assert progress_path.is_dir(), "Hiányzik az app/services/ mappa."

    # Keressünk progress-hez kapcsolódó fájlt
    service_files = list(progress_path.glob("*.py"))
    service_names = [f.stem for f in service_files]
    assert "progress" in service_names or "github" in service_names, (
        "Hiányzik az app/services/progress.py vagy app/services/github.py."
    )
