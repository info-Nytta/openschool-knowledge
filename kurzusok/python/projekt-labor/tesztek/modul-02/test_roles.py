"""
Modul 2 — Felhasználókezelés: Szerepkörök verifikáció.
Ellenőrzi, hogy a szerepkör-alapú hozzáférés-vezérlés implementálva van.
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent


def _setup_backend():
    backend_path = REPO_ROOT / "backend"
    if str(backend_path) not in sys.path:
        sys.path.insert(0, str(backend_path))


def test_user_role_has_three_values():
    """A UserRole enum-nak legalább 3 értéke van (student, mentor, admin)."""
    _setup_backend()
    from app.models.user import UserRole
    roles = list(UserRole)
    assert len(roles) >= 3, (
        f"A UserRole enum-nak legalább 3 értéke legyen "
        f"(student, mentor, admin). Jelenleg: {len(roles)}"
    )


def test_user_default_role_is_student():
    """A User modell alapértelmezett role-ja student."""
    _setup_backend()
    from app.models.user import User, UserRole
    role_column = User.__table__.columns["role"]
    # Az alapértelmezett értéket a column default-ból ellenőrizzük
    if role_column.default is not None:
        default_val = role_column.default.arg
        if callable(default_val):
            default_val = default_val(None)
        assert default_val == UserRole.student or default_val == "student", (
            f"A User alapértelmezett role-ja legyen 'student', jelenleg: {default_val}"
        )


def test_jwt_creates_valid_tokens():
    """A JWT modul tud access és refresh token-t generálni."""
    _setup_backend()
    try:
        from app.auth.jwt import create_access_token, create_refresh_token
        access = create_access_token(user_id=1)
        assert isinstance(access, str) and len(access) > 20, (
            "Az access token legyen egy nem üres string."
        )
        refresh = create_refresh_token(user_id=1)
        assert isinstance(refresh, str) and len(refresh) > 20, (
            "A refresh token legyen egy nem üres string."
        )
        assert access != refresh, (
            "Az access és refresh token nem lehet ugyanaz."
        )
    except ImportError as e:
        assert False, f"JWT import hiba: {e}"
