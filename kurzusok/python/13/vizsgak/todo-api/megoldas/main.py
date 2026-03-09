from fastapi import FastAPI, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date

from database import engine, get_db, Base
from models import TodoModel
from schemas import TodoCreate, TodoUpdate
from auth import router as auth_router, get_current_user

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_router)


def todok_betoltese(db: Session):
    if db.query(TodoModel).count() > 0:
        return
    try:
        with open("todok.txt", "r", encoding="utf-8") as f:
            for sor in f:
                adatok = sor.strip().split(";")
                todo = TodoModel(
                    cim=adatok[0],
                    leiras=adatok[1],
                    prioritas=int(adatok[2]),
                    hatarido=adatok[3] if adatok[3] else None,
                    kesz=adatok[4] == "True",
                    letrehozva=date.today().isoformat(),
                )
                db.add(todo)
        db.commit()
    except FileNotFoundError:
        pass


@app.on_event("startup")
def startup():
    db = next(get_db())
    try:
        todok_betoltese(db)
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Todo API"}


@app.get("/todos/statisztika")
def todos_statisztika(db: Session = Depends(get_db)):
    osszes = db.query(TodoModel).count()
    kesz = db.query(TodoModel).filter(TodoModel.kesz == True).count()
    return {"osszes": osszes, "kesz": kesz, "hatra_van": osszes - kesz}


@app.get("/todos")
def get_todos(
    kesz: Optional[bool] = None,
    min_prioritas: Optional[int] = Query(default=None, ge=1, le=5),
    db: Session = Depends(get_db),
):
    query = db.query(TodoModel)
    if kesz is not None:
        query = query.filter(TodoModel.kesz == kesz)
    if min_prioritas is not None:
        query = query.filter(TodoModel.prioritas >= min_prioritas)
    return query.all()


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo nem található")
    return todo


@app.post("/todos", status_code=201)
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    uj_todo = TodoModel(
        cim=todo.cim,
        leiras=todo.leiras,
        prioritas=todo.prioritas,
        hatarido=todo.hatarido,
        letrehozva=date.today().isoformat(),
    )
    db.add(uj_todo)
    db.commit()
    db.refresh(uj_todo)
    return uj_todo


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    meglevo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not meglevo:
        raise HTTPException(status_code=404, detail="Todo nem található")
    update_data = todo.model_dump(exclude_unset=True)
    for kulcs, ertek in update_data.items():
        setattr(meglevo, kulcs, ertek)
    db.commit()
    db.refresh(meglevo)
    return meglevo


@app.delete("/todos/{todo_id}")
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo nem található")
    db.delete(todo)
    db.commit()
    return {"message": "Todo törölve"}
