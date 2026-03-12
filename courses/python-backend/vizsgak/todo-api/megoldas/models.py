from sqlalchemy import Column, Integer, String, Boolean
from datetime import date
from database import Base


class TodoModel(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    cim = Column(String, nullable=False)
    leiras = Column(String, nullable=True)
    prioritas = Column(Integer, default=3)
    hatarido = Column(String, nullable=True)
    kesz = Column(Boolean, default=False)
    letrehozva = Column(String, default=lambda: date.today().isoformat())


class FelhasznaloModel(Base):
    __tablename__ = "felhasznalok"

    id = Column(Integer, primary_key=True, index=True)
    felhasznalonev = Column(String, unique=True, nullable=False)
    jelszo_hash = Column(String, nullable=False)
