from fastapi import FastAPI, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date

from database import engine, get_db, Base
from models import TermekModel
from schemas import TermekCreate, TermekUpdate
from auth import router as auth_router, get_current_user

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_router)


def termekek_betoltese(db: Session):
    if db.query(TermekModel).count() > 0:
        return
    try:
        with open("termekek.txt", "r", encoding="utf-8") as f:
            for sor in f:
                adatok = sor.strip().split(";")
                termek = TermekModel(
                    nev=adatok[0],
                    leiras=adatok[1],
                    ar=int(adatok[2]),
                    kategoria=adatok[3],
                    keszlet=int(adatok[4]),
                    aktiv=adatok[5] == "True",
                    letrehozva=date.today().isoformat(),
                )
                db.add(termek)
        db.commit()
    except FileNotFoundError:
        pass


@app.on_event("startup")
def startup():
    db = next(get_db())
    try:
        termekek_betoltese(db)
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Webshop API"}


@app.get("/termekek/statisztika")
def termekek_statisztika(db: Session = Depends(get_db)):
    osszes = db.query(TermekModel).count()
    keszleten = db.query(TermekModel).filter(TermekModel.keszlet > 0).count()
    arak = [t.ar for t in db.query(TermekModel).all()]
    atlag = round(sum(arak) / len(arak), 1) if arak else 0.0
    return {"osszes": osszes, "keszleten": keszleten, "kifogyott": osszes - keszleten, "atlag_ar": atlag}


@app.get("/termekek")
def get_termekek(
    kategoria: Optional[str] = None,
    min_ar: Optional[int] = Query(default=None, ge=0),
    max_ar: Optional[int] = Query(default=None, ge=0),
    db: Session = Depends(get_db),
):
    query = db.query(TermekModel)
    if kategoria is not None:
        query = query.filter(TermekModel.kategoria == kategoria)
    if min_ar is not None:
        query = query.filter(TermekModel.ar >= min_ar)
    if max_ar is not None:
        query = query.filter(TermekModel.ar <= max_ar)
    return query.all()


@app.get("/termekek/{termek_id}")
def get_termek(termek_id: int, db: Session = Depends(get_db)):
    termek = db.query(TermekModel).filter(TermekModel.id == termek_id).first()
    if not termek:
        raise HTTPException(status_code=404, detail="Termék nem található")
    return termek


@app.post("/termekek", status_code=201)
def create_termek(
    termek: TermekCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    uj_termek = TermekModel(
        nev=termek.nev,
        leiras=termek.leiras,
        ar=termek.ar,
        kategoria=termek.kategoria,
        keszlet=termek.keszlet,
        letrehozva=date.today().isoformat(),
    )
    db.add(uj_termek)
    db.commit()
    db.refresh(uj_termek)
    return uj_termek


@app.put("/termekek/{termek_id}")
def update_termek(termek_id: int, termek: TermekUpdate, db: Session = Depends(get_db)):
    meglevo = db.query(TermekModel).filter(TermekModel.id == termek_id).first()
    if not meglevo:
        raise HTTPException(status_code=404, detail="Termék nem található")
    update_data = termek.model_dump(exclude_unset=True)
    for kulcs, ertek in update_data.items():
        setattr(meglevo, kulcs, ertek)
    db.commit()
    db.refresh(meglevo)
    return meglevo


@app.delete("/termekek/{termek_id}")
def delete_termek(
    termek_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    termek = db.query(TermekModel).filter(TermekModel.id == termek_id).first()
    if not termek:
        raise HTTPException(status_code=404, detail="Termék nem található")
    db.delete(termek)
    db.commit()
    return {"message": "Termék törölve"}
