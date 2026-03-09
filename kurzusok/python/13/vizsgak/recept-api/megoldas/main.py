from fastapi import FastAPI, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date

from database import engine, get_db, Base
from models import ReceptModel
from schemas import ReceptCreate, ReceptUpdate
from auth import router as auth_router, get_current_user

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_router)


def receptek_betoltese(db: Session):
    if db.query(ReceptModel).count() > 0:
        return
    try:
        with open("receptek.txt", "r", encoding="utf-8") as f:
            for sor in f:
                adatok = sor.strip().split(";")
                recept = ReceptModel(
                    nev=adatok[0],
                    leiras=adatok[1],
                    kategoria=adatok[2],
                    elkeszitesi_ido=int(adatok[3]),
                    kaloria=int(adatok[4]),
                    kedvenc=adatok[5] == "True",
                    letrehozva=date.today().isoformat(),
                )
                db.add(recept)
        db.commit()
    except FileNotFoundError:
        pass


@app.on_event("startup")
def startup():
    db = next(get_db())
    try:
        receptek_betoltese(db)
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Recept API"}


@app.get("/receptek/statisztika")
def receptek_statisztika(db: Session = Depends(get_db)):
    osszes = db.query(ReceptModel).count()
    kedvenc = db.query(ReceptModel).filter(ReceptModel.kedvenc == True).count()
    all_receptek = db.query(ReceptModel).all()
    atlag_ido = round(sum(r.elkeszitesi_ido for r in all_receptek) / osszes, 1) if osszes else 0.0
    atlag_kal = round(sum(r.kaloria for r in all_receptek) / osszes, 1) if osszes else 0.0
    return {"osszes": osszes, "kedvenc": kedvenc, "atlag_ido": atlag_ido, "atlag_kaloria": atlag_kal}


@app.get("/receptek")
def get_receptek(
    kategoria: Optional[str] = None,
    max_ido: Optional[int] = Query(default=None, ge=1),
    db: Session = Depends(get_db),
):
    query = db.query(ReceptModel)
    if kategoria is not None:
        query = query.filter(ReceptModel.kategoria == kategoria)
    if max_ido is not None:
        query = query.filter(ReceptModel.elkeszitesi_ido <= max_ido)
    return query.all()


@app.get("/receptek/{recept_id}")
def get_recept(recept_id: int, db: Session = Depends(get_db)):
    recept = db.query(ReceptModel).filter(ReceptModel.id == recept_id).first()
    if not recept:
        raise HTTPException(status_code=404, detail="Recept nem található")
    return recept


@app.post("/receptek", status_code=201)
def create_recept(
    recept: ReceptCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    uj_recept = ReceptModel(
        nev=recept.nev,
        leiras=recept.leiras,
        kategoria=recept.kategoria,
        elkeszitesi_ido=recept.elkeszitesi_ido,
        kaloria=recept.kaloria,
        letrehozva=date.today().isoformat(),
    )
    db.add(uj_recept)
    db.commit()
    db.refresh(uj_recept)
    return uj_recept


@app.put("/receptek/{recept_id}")
def update_recept(recept_id: int, recept: ReceptUpdate, db: Session = Depends(get_db)):
    meglevo = db.query(ReceptModel).filter(ReceptModel.id == recept_id).first()
    if not meglevo:
        raise HTTPException(status_code=404, detail="Recept nem található")
    update_data = recept.model_dump(exclude_unset=True)
    for kulcs, ertek in update_data.items():
        setattr(meglevo, kulcs, ertek)
    db.commit()
    db.refresh(meglevo)
    return meglevo


@app.delete("/receptek/{recept_id}")
def delete_recept(
    recept_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    recept = db.query(ReceptModel).filter(ReceptModel.id == recept_id).first()
    if not recept:
        raise HTTPException(status_code=404, detail="Recept nem található")
    db.delete(recept)
    db.commit()
    return {"message": "Recept törölve"}
