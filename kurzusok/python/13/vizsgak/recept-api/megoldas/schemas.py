from pydantic import BaseModel, Field
from typing import Optional


class ReceptCreate(BaseModel):
    nev: str = Field(min_length=3)
    leiras: Optional[str] = None
    kategoria: str = Field(min_length=2)
    elkeszitesi_ido: int = Field(ge=1)
    kaloria: int = Field(default=0, ge=0)


class ReceptRead(BaseModel):
    id: int
    nev: str
    leiras: Optional[str] = None
    kategoria: str
    elkeszitesi_ido: int
    kaloria: int
    kedvenc: bool = False
    letrehozva: str

    class Config:
        from_attributes = True


class ReceptUpdate(BaseModel):
    nev: Optional[str] = None
    leiras: Optional[str] = None
    kategoria: Optional[str] = None
    elkeszitesi_ido: Optional[int] = Field(default=None, ge=1)
    kaloria: Optional[int] = Field(default=None, ge=0)
    kedvenc: Optional[bool] = None


class FelhasznaloCreate(BaseModel):
    felhasznalonev: str = Field(min_length=3)
    jelszo: str = Field(min_length=6)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
