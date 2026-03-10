# Modul 4 — Tanúsítvány rendszer

## Cél

Automatikus tanúsítvány generálás kurzus befejezésekor. A modul végére:

- A rendszer felismeri, mikor fejezte be valaki a kurzust
- PDF tanúsítvány generálódik egyedi azonosítóval és QR kóddal
- Publikus verifikációs endpoint: bárki ellenőrizheti a tanúsítvány hitelességét

## 4.1 Completion logika

Mikor tekinthető befejezettnek egy kurzus?

**Szabály:** Minden kötelező feladat (`Exercise`) `completed` státuszban van.

```python
# app/services/certificate.py

def is_course_completed(db: Session, user_id: int, course_id: int) -> bool:
    total = db.query(Exercise).join(Module).filter(
        Module.course_id == course_id,
        Exercise.required == True
    ).count()

    completed = db.query(Progress).join(Exercise).join(Module).filter(
        Module.course_id == course_id,
        Progress.user_id == user_id,
        Progress.status == ProgressStatus.completed,
        Exercise.required == True
    ).count()

    return total > 0 and total == completed
```

**Feladat:**
- Adj hozzá egy `required` mezőt az `Exercise` modellhez (default: `True`)
- Implementáld a completion check logikát
- Teszteld: részben kész kurzus → False, teljesen kész → True

## 4.2 Certificate modell

```python
# app/models/certificate.py
import uuid
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
from datetime import datetime, timezone

class Certificate(Base):
    __tablename__ = "certificates"

    id = Column(Integer, primary_key=True)
    cert_id = Column(String, unique=True, nullable=False,
                     default=lambda: str(uuid.uuid4()))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    issued_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    pdf_path = Column(String)
```

**Feladat:**
- Hozd létre a Certificate modellt
- A `cert_id` UUID formátumú, egyedi azonosító
- Generálj Alembic migrációt
- Egyedi constraint: egy user egy kurzushoz csak egy tanúsítványt kaphat

## 4.3 PDF generálás

Két lehetőség:

| Könyvtár | Előny | Hátrány |
|----------|-------|---------|
| ReportLab | Könnyű, nincs rendszer-függőség | Alacsony szintű API, nehéz szép dizájnt csinálni |
| WeasyPrint | HTML/CSS → PDF, szép eredmény | Rendszer-függőségek (GTK, Pango) |

**Ajánlott: WeasyPrint** — HTML sablonból generálunk PDF-et, a dizájn CSS-sel módosítható.

```python
# app/services/pdf.py
from weasyprint import HTML
from pathlib import Path

TEMPLATE_DIR = Path(__file__).parent.parent / "templates"

def generate_certificate_pdf(
    name: str,
    course_name: str,
    cert_id: str,
    issued_date: str,
    verify_url: str
) -> bytes:
    html_content = (TEMPLATE_DIR / "certificate.html").read_text()
    html_content = html_content.replace("{{name}}", name)
    html_content = html_content.replace("{{course_name}}", course_name)
    html_content = html_content.replace("{{cert_id}}", cert_id)
    html_content = html_content.replace("{{issued_date}}", issued_date)
    html_content = html_content.replace("{{verify_url}}", verify_url)

    return HTML(string=html_content).write_pdf()
```

**Feladat:**
- Válaszd ki a PDF könyvtárat és add hozzá a `requirements.txt`-hez
- Hozz létre egy HTML tanúsítvány sablont (`templates/certificate.html`)
- A sablon tartalmazza: név, kurzus neve, dátum, tanúsítvány ID, QR kód
- Teszteld: generálj egy minta PDF-et

## 4.4 QR kód

A tanúsítványon legyen egy QR kód, ami a verifikációs URL-re mutat.

```python
# app/services/qr.py
import qrcode
import io
import base64

def generate_qr_base64(url: str) -> str:
    qr = qrcode.make(url)
    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()
```

**Feladat:**
- Add hozzá a `qrcode` csomagot a `requirements.txt`-hez
- A QR kód a verifikációs URL-re mutasson: `https://devschool.hu/verify/{cert_id}`
- A QR kódot base64 PNG-ként ágyazd be a HTML sablonba

## 4.5 API endpoint-ok

| Endpoint | Metódus | Jogosultság | Leírás |
|----------|---------|-------------|--------|
| `/api/me/certificates` | GET | autentikált | Saját tanúsítványaim listája |
| `/api/me/courses/{id}/certificate` | POST | autentikált | Tanúsítvány igénylése (ha kész a kurzus) |
| `/api/me/certificates/{cert_id}/pdf` | GET | autentikált | PDF letöltése |
| `/api/verify/{cert_id}` | GET | nyilvános | Tanúsítvány hitelesítés |

**A tanúsítvány igénylés flow-ja:**
1. Felhasználó hívja: `POST /api/me/courses/{id}/certificate`
2. Backend ellenőrzi: minden kötelező feladat kész?
3. Ha igen → Certificate rekord létrejön + PDF generálódik
4. Ha nem → 400 hibaüzenet: "A kurzus még nincs befejezve"
5. Ha már van tanúsítvány → 409: "Már van tanúsítványod ehhez a kurzushoz"

**Verifikációs endpoint válasz:**
```json
{
  "valid": true,
  "name": "Kiss Péter",
  "course": "Python alapok",
  "issued_at": "2025-06-15T12:00:00Z",
  "cert_id": "a1b2c3d4-..."
}
```

**Feladat:**
- Implementáld mind a 4 endpoint-ot
- A PDF fájlokat tárold a szerveren (pl. `data/certificates/` mappa)
- A verifikációs endpoint legyen publikus (nem kell token)

## 4.6 Tesztek

**Tesztelendő esetek:**
- Completion check: részben kész → False, teljesen kész → True
- Tanúsítvány igénylés: kész kurzus → 201, nem kész → 400, duplikált → 409
- Verifikáció: létező cert_id → valid, nem létező → 404
- PDF generálás: a fájl létrejön és nem üres

**Feladat:**
- Írj teszteket minden fenti esetre
- A PDF generálást mockold a tesztekben (gyorsabb, nincs WeasyPrint függőség)
- `pytest -v` → minden zöld

## Háttéranyag

Ezeket nem kell elejétől végig elolvasni — használd referenciaként, amikor az adott témánál tartasz.

| Téma | Link | Miért hasznos |
|------|------|---------------|
| WeasyPrint | [doc.courtbouillon.org/weasyprint](https://doc.courtbouillon.org/weasyprint/stable/) | HTML → PDF konvertálás Python-ban |
| ReportLab (alternatíva) | [docs.reportlab.com](https://docs.reportlab.com/) | PDF generálás programozottan (ha nem HTML-ből) |
| python-qrcode | [github.com/lincolnloop/python-qrcode](https://github.com/lincolnloop/python-qrcode) | QR kód generálás a verifikációs URL-hez |
| Jinja2 Templates | [jinja.palletsprojects.com](https://jinja.palletsprojects.com/) | HTML sablonok a tanúsítványhoz |
| UUID | [docs.python.org/3/library/uuid.html](https://docs.python.org/3/library/uuid.html) | Egyedi tanúsítvány azonosítók generálása |

## Verifikációs tesztek

A modul végén futtasd a verifikációs teszteket:

```bash
cd devschool-platform
pytest tesztek/modul-04/ -v
```

**Mit ellenőriznek a tesztek:**

| Tesztfájl | Ellenőrzések |
|-----------|---------------|
| `test_completion.py` | Certificate modell létezik (cert_id, user_id, course_id); `is_course_completed` függvény; Exercise-nek van `required` mezője; PDF és certificate HTML sablon létezik |
| `test_verify.py` | Verifikációs endpoint létezik; nem létező cert_id → 404; tanúsítvány igénylés és listázás auth-ot igényel; QR modul létezik |

> **Megjegyzés:** A verifikációs tesztek a PDF generálást nem futtatják (nincs WeasyPrint függőség), csak a fájlok létezését ellenőrzik. A részletes PDF teszt a **saját tesztek** feladata.

## Ellenőrzőlista

- [ ] Completion logika helyesen működik
- [ ] Certificate modell és migráció kész
- [ ] PDF tanúsítvány generálódik QR kóddal
- [ ] Tanúsítvány igénylés API működik (kész kurzus kell hozzá)
- [ ] Verifikációs endpoint publikusan elérhető
- [ ] Saját tesztek lefedik a completion, igénylés, verifikáció eseteket
- [ ] `pytest tesztek/modul-04/ -v` → minden zöld (verifikációs tesztek)
