from sqlalchemy import Column, Integer, String, Boolean
from datetime import date
from database import Base


class PostModel(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    cim = Column(String, nullable=False)
    tartalom = Column(String, nullable=False)
    szerzo = Column(String, nullable=False)
    cimke = Column(String, nullable=True)
    publikalva = Column(Boolean, default=False)
    letrehozva = Column(String, default=lambda: date.today().isoformat())


class FelhasznaloModel(Base):
    __tablename__ = "felhasznalok"

    id = Column(Integer, primary_key=True, index=True)
    felhasznalonev = Column(String, unique=True, nullable=False)
    jelszo_hash = Column(String, nullable=False)
