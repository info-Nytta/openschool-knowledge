"""
Modul 2 — Felhasználókezelés: Védett endpoint-ok verifikáció.
Ellenőrzi, hogy a védett endpoint-ok megfelelően kezelik a tokeneket.
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


def test_me_without_token_returns_401():
    """/api/auth/me token nélkül → 401."""
    client = _get_client()
    response = client.get("/api/auth/me")
    assert response.status_code in (401, 403), (
        f"Elvárt: 401 vagy 403, kapott: {response.status_code}"
    )


def test_me_with_invalid_token_returns_401():
    """/api/auth/me érvénytelen token-nel → 401."""
    client = _get_client()
    response = client.get(
        "/api/auth/me",
        headers={"Authorization": "Bearer invalid_token_12345"}
    )
    assert response.status_code in (401, 403), (
        f"Érvénytelen token-nel elvárt: 401 vagy 403, kapott: {response.status_code}"
    )


def test_auth_dependencies_exist():
    """A get_current_user és require_role dependency-k léteznek."""
    _setup_backend()
    try:
        from app.auth.dependencies import get_current_user
        assert callable(get_current_user), "A get_current_user legyen callable."
    except ImportError:
        assert False, (
            "Nem sikerült importálni: from app.auth.dependencies import get_current_user. "
            "Hozd létre az auth middleware-t."
        )


def test_require_role_dependency_exists():
    """A require_role dependency létezik."""
    _setup_backend()
    try:
        from app.auth.dependencies import require_role
        assert callable(require_role), "A require_role legyen callable."
    except ImportError:
        assert False, (
            "Nem sikerült importálni: from app.auth.dependencies import require_role."
        )
