"""
Modul 4 — Tanúsítvány rendszer: Verifikációs endpoint verifikáció.
Ellenőrzi, hogy a tanúsítvány API endpoint-ok léteznek és megfelelően működnek.
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


def test_verify_endpoint_exists():
    """A /api/verify/{cert_id} endpoint létezik."""
    _setup_backend()
    from app.main import app
    routes = [route.path for route in app.routes]
    assert any("verify" in r for r in routes), (
        "A verifikációs endpoint nem található. "
        "Hozd létre: GET /api/verify/{cert_id}"
    )


def test_verify_nonexistent_returns_404():
    """Nem létező cert_id-vel 404-et kapunk."""
    client = _get_client()
    response = client.get("/api/verify/nonexistent-cert-id-12345")
    assert response.status_code == 404, (
        f"Nem létező tanúsítvánnyal elvárt: 404, kapott: {response.status_code}"
    )


def test_certificate_request_requires_auth():
    """A tanúsítvány igénylés autentikációt igényel."""
    client = _get_client()
    response = client.post("/api/me/courses/1/certificate")
    assert response.status_code in (401, 403), (
        f"A tanúsítvány igénylés token nélkül "
        f"{response.status_code}-et adott vissza. Elvárt: 401 vagy 403."
    )


def test_my_certificates_requires_auth():
    """A saját tanúsítványok listázása autentikációt igényel."""
    client = _get_client()
    response = client.get("/api/me/certificates")
    assert response.status_code in (401, 403), (
        f"A /api/me/certificates endpoint token nélkül "
        f"{response.status_code}-et adott vissza. Elvárt: 401 vagy 403."
    )


def test_qr_module_exists():
    """A QR kód generálás service létezik."""
    _setup_backend()
    qr_path = REPO_ROOT / "backend" / "app" / "services" / "qr.py"
    assert qr_path.is_file(), (
        "Hiányzik az app/services/qr.py. "
        "Hozd létre a QR kód generáló service-t."
    )
