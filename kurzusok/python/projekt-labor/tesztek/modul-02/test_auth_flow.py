"""
Modul 2 — Felhasználókezelés: Auth flow verifikáció.
Ellenőrzi, hogy az auth endpoint-ok léteznek és az OAuth flow működik.
"""

import sys
from pathlib import Path
from unittest.mock import patch, AsyncMock

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


def test_auth_login_endpoint_exists():
    """A /api/auth/login endpoint létezik."""
    _setup_backend()
    from app.main import app
    routes = [route.path for route in app.routes]
    assert any("auth" in r and "login" in r for r in routes), (
        "Az auth login endpoint nem található. "
        "Hozd létre: GET /api/auth/login"
    )


def test_auth_callback_endpoint_exists():
    """A /api/auth/callback endpoint létezik."""
    _setup_backend()
    from app.main import app
    routes = [route.path for route in app.routes]
    assert any("auth" in r and "callback" in r for r in routes), (
        "Az auth callback endpoint nem található. "
        "Hozd létre: GET /api/auth/callback"
    )


def test_auth_me_endpoint_exists():
    """A /api/auth/me endpoint létezik."""
    _setup_backend()
    from app.main import app
    routes = [route.path for route in app.routes]
    assert any("auth" in r and "me" in r for r in routes), (
        "Az auth me endpoint nem található. "
        "Hozd létre: GET /api/auth/me"
    )


def test_auth_me_requires_token():
    """A /api/auth/me endpoint 401/403-at ad vissza token nélkül."""
    client = _get_client()
    response = client.get("/api/auth/me")
    assert response.status_code in (401, 403), (
        f"A /api/auth/me endpoint {response.status_code}-et adott vissza "
        f"token nélkül. Elvárt: 401 vagy 403."
    )


def test_user_model_exists():
    """A User modell létezik."""
    _setup_backend()
    try:
        from app.models.user import User
        assert hasattr(User, "__tablename__"), "A User modellnek legyen __tablename__ attribútuma."
        assert hasattr(User, "github_id"), "A User modellnek legyen github_id mezője."
        assert hasattr(User, "username"), "A User modellnek legyen username mezője."
        assert hasattr(User, "role"), "A User modellnek legyen role mezője."
    except ImportError:
        assert False, (
            "Nem sikerült importálni: from app.models.user import User. "
            "Hozd létre a User modellt."
        )


def test_user_role_enum_exists():
    """A UserRole enum létezik a megfelelő értékekkel."""
    _setup_backend()
    try:
        from app.models.user import UserRole
        roles = [r.value for r in UserRole]
        assert "student" in roles, "A UserRole enum-ban legyen 'student' érték."
        assert "admin" in roles, "A UserRole enum-ban legyen 'admin' érték."
    except ImportError:
        assert False, (
            "Nem sikerült importálni: from app.models.user import UserRole."
        )


def test_jwt_module_exists():
    """A JWT modul létezik."""
    _setup_backend()
    jwt_path = REPO_ROOT / "backend" / "app" / "auth"
    assert jwt_path.is_dir(), (
        "Hiányzik az app/auth/ mappa. "
        "Hozd létre a JWT token kezelés logikáját."
    )
