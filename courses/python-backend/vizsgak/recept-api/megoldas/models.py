from sqlalchemy import Column, Integer, String, Boolean
from datetime import date
from database import Base


class ReceptModel(Base):
    __tablename__ = "receptek"

    id = Column(Integer, primary_key=True, index=True)
    nev = Column(String, nullable=False)
    leiras = Column(String, nullable=True)
    kategoria = Column(String, nullable=False)
    elkeszitesi_ido = Column(Integer, nullable=False)
    kaloria = Column(Integer, default=0)
    kedvenc = Column(Boolean, default=False)
    letrehozva = Column(String, default=lambda: date.today().isoformat())


class FelhasznaloModel(Base):
    __tablename__ = "felhasznalok"

    id = Column(Integer, primary_key=True, index=True)
    felhasznalonev = Column(String, unique=True, nullable=False)
    jelszo_hash = Column(String, nullable=False)
