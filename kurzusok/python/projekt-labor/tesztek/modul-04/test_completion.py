"""
Modul 4 — Tanúsítvány rendszer: Completion logika verifikáció.
Ellenőrzi, hogy a kurzus befejezés és tanúsítvány generálás implementálva van.
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent


def _setup_backend():
    backend_path = REPO_ROOT / "backend"
    if str(backend_path) not in sys.path:
        sys.path.insert(0, str(backend_path))


def test_certificate_model_exists():
    """A Certificate modell létezik."""
    _setup_backend()
    try:
        from app.models.certificate import Certificate
        assert hasattr(Certificate, "__tablename__")
        assert hasattr(Certificate, "cert_id"), (
            "A Certificate modellnek legyen cert_id mezője (UUID)."
        )
        assert hasattr(Certificate, "user_id"), (
            "A Certificate modellnek legyen user_id mezője."
        )
        assert hasattr(Certificate, "course_id"), (
            "A Certificate modellnek legyen course_id mezője."
        )
    except ImportError:
        assert False, (
            "Nem sikerült importálni: from app.models.certificate import Certificate"
        )


def test_completion_function_exists():
    """A kurzus completion ellenőrző függvény létezik."""
    _setup_backend()
    try:
        from app.services.certificate import is_course_completed
        assert callable(is_course_completed)
    except ImportError:
        assert False, (
            "Nem sikerült importálni: "
            "from app.services.certificate import is_course_completed"
        )


def test_exercise_has_required_field():
    """Az Exercise modellnek van required mezője."""
    _setup_backend()
    try:
        from app.models.course import Exercise
    except ImportError:
        from app.models.exercise import Exercise

    assert hasattr(Exercise, "required"), (
        "Az Exercise modellnek legyen 'required' mezője (Boolean, default True)."
    )


def test_pdf_service_exists():
    """A PDF generálás service létezik."""
    _setup_backend()
    pdf_path = REPO_ROOT / "backend" / "app" / "services" / "pdf.py"
    assert pdf_path.is_file(), (
        "Hiányzik az app/services/pdf.py. "
        "Hozd létre a PDF tanúsítvány generáló service-t."
    )


def test_certificate_template_exists():
    """A tanúsítvány HTML sablon létezik."""
    _setup_backend()
    template_paths = [
        REPO_ROOT / "backend" / "app" / "templates" / "certificate.html",
        REPO_ROOT / "backend" / "templates" / "certificate.html",
    ]
    assert any(p.is_file() for p in template_paths), (
        "Hiányzik a certificate.html sablon. "
        "Hozd létre a templates/ mappában."
    )
