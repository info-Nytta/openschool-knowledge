from fastapi import FastAPI, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date

from database import engine, get_db, Base
from models import PostModel
from schemas import PostCreate, PostUpdate
from auth import router as auth_router, get_current_user

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_router)


def posztok_betoltese(db: Session):
    if db.query(PostModel).count() > 0:
        return
    try:
        with open("posztok.txt", "r", encoding="utf-8") as f:
            for sor in f:
                adatok = sor.strip().split(";")
                poszt = PostModel(
                    cim=adatok[0],
                    tartalom=adatok[1],
                    szerzo=adatok[2],
                    cimke=adatok[3] if adatok[3] else None,
                    publikalva=adatok[4] == "True",
                    letrehozva=date.today().isoformat(),
                )
                db.add(poszt)
        db.commit()
    except FileNotFoundError:
        pass


@app.on_event("startup")
def startup():
    db = next(get_db())
    try:
        posztok_betoltese(db)
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Blog API"}


@app.get("/posts/statisztika")
def posts_statisztika(db: Session = Depends(get_db)):
    osszes = db.query(PostModel).count()
    publikus = db.query(PostModel).filter(PostModel.publikalva == True).count()
    return {"osszes": osszes, "publikus": publikus, "piszkozat": osszes - publikus}


@app.get("/posts")
def get_posts(
    publikalva: Optional[bool] = None,
    cimke: Optional[str] = None,
    db: Session = Depends(get_db),
):
    query = db.query(PostModel)
    if publikalva is not None:
        query = query.filter(PostModel.publikalva == publikalva)
    if cimke is not None:
        query = query.filter(PostModel.cimke == cimke)
    return query.all()


@app.get("/posts/{post_id}")
def get_post(post_id: int, db: Session = Depends(get_db)):
    poszt = db.query(PostModel).filter(PostModel.id == post_id).first()
    if not poszt:
        raise HTTPException(status_code=404, detail="Poszt nem található")
    return poszt


@app.post("/posts", status_code=201)
def create_post(
    poszt: PostCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    uj_poszt = PostModel(
        cim=poszt.cim,
        tartalom=poszt.tartalom,
        szerzo=poszt.szerzo,
        cimke=poszt.cimke,
        letrehozva=date.today().isoformat(),
    )
    db.add(uj_poszt)
    db.commit()
    db.refresh(uj_poszt)
    return uj_poszt


@app.put("/posts/{post_id}")
def update_post(post_id: int, poszt: PostUpdate, db: Session = Depends(get_db)):
    meglevo = db.query(PostModel).filter(PostModel.id == post_id).first()
    if not meglevo:
        raise HTTPException(status_code=404, detail="Poszt nem található")
    update_data = poszt.model_dump(exclude_unset=True)
    for kulcs, ertek in update_data.items():
        setattr(meglevo, kulcs, ertek)
    db.commit()
    db.refresh(meglevo)
    return meglevo


@app.delete("/posts/{post_id}")
def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    poszt = db.query(PostModel).filter(PostModel.id == post_id).first()
    if not poszt:
        raise HTTPException(status_code=404, detail="Poszt nem található")
    db.delete(poszt)
    db.commit()
    return {"message": "Poszt törölve"}
