from sqlalchemy import Column, Integer, String, Boolean
from datetime import date
from database import Base


class TermekModel(Base):
    __tablename__ = "termekek"

    id = Column(Integer, primary_key=True, index=True)
    nev = Column(String, nullable=False)
    leiras = Column(String, nullable=True)
    ar = Column(Integer, nullable=False)
    kategoria = Column(String, nullable=False)
    keszlet = Column(Integer, default=0)
    aktiv = Column(Boolean, default=True)
    letrehozva = Column(String, default=lambda: date.today().isoformat())


class FelhasznaloModel(Base):
    __tablename__ = "felhasznalok"

    id = Column(Integer, primary_key=True, index=True)
    felhasznalonev = Column(String, unique=True, nullable=False)
    jelszo_hash = Column(String, nullable=False)
