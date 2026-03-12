"""
Modul 3 — Kurzusok és haladás: CRUD és beiratkozás verifikáció.
Ellenőrzi, hogy a kurzus modellek és endpoint-ok léteznek.
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


def test_course_model_exists():
    """A Course modell létezik."""
    _setup_backend()
    try:
        from app.models.course import Course
        assert hasattr(Course, "__tablename__"), "A Course modellnek legyen __tablename__-je."
    except ImportError:
        assert False, "Nem sikerült importálni: from app.models.course import Course"


def test_module_model_exists():
    """A Module modell létezik."""
    _setup_backend()
    try:
        from app.models.course import Module
        assert hasattr(Module, "__tablename__")
    except ImportError:
        try:
            from app.models.module import Module
            assert hasattr(Module, "__tablename__")
        except ImportError:
            assert False, "Nem sikerült importálni a Module modellt."


def test_exercise_model_exists():
    """Az Exercise modell létezik."""
    _setup_backend()
    try:
        from app.models.course import Exercise
    except ImportError:
        try:
            from app.models.exercise import Exercise
        except ImportError:
            assert False, "Nem sikerült importálni az Exercise modellt."


def test_enrollment_model_exists():
    """Az Enrollment modell létezik."""
    _setup_backend()
    try:
        from app.models.course import Enrollment
    except ImportError:
        try:
            from app.models.enrollment import Enrollment
        except ImportError:
            assert False, "Nem sikerült importálni az Enrollment modellt."


def test_progress_model_exists():
    """A Progress modell létezik."""
    _setup_backend()
    try:
        from app.models.progress import Progress
    except ImportError:
        try:
            from app.models.course import Progress
        except ImportError:
            assert False, "Nem sikerült importálni a Progress modellt."


def test_courses_list_endpoint():
    """A GET /api/courses endpoint létezik és nyilvános."""
    client = _get_client()
    response = client.get("/api/courses")
    assert response.status_code == 200, (
        f"A GET /api/courses endpoint {response.status_code}-et adott vissza. "
        f"Elvárt: 200 (nyilvános endpoint)."
    )


def test_courses_list_returns_list():
    """A GET /api/courses listát ad vissza."""
    client = _get_client()
    response = client.get("/api/courses")
    if response.status_code == 200:
        data = response.json()
        assert isinstance(data, list), (
            "A GET /api/courses válasza legyen egy lista."
        )


def test_enroll_requires_auth():
    """A beiratkozás endpoint autentikációt igényel."""
    client = _get_client()
    response = client.post("/api/courses/1/enroll")
    assert response.status_code in (401, 403, 422), (
        f"A POST /api/courses/1/enroll endpoint token nélkül "
        f"ne engedjen beiratkozni. Kapott: {response.status_code}"
    )
