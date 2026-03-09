from pydantic import BaseModel, Field
from typing import Optional


class TermekCreate(BaseModel):
    nev: str = Field(min_length=3)
    leiras: Optional[str] = None
    ar: int = Field(ge=1)
    kategoria: str = Field(min_length=2)
    keszlet: int = Field(default=0, ge=0)


class TermekRead(BaseModel):
    id: int
    nev: str
    leiras: Optional[str] = None
    ar: int
    kategoria: str
    keszlet: int
    aktiv: bool = True
    letrehozva: str

    class Config:
        from_attributes = True


class TermekUpdate(BaseModel):
    nev: Optional[str] = None
    leiras: Optional[str] = None
    ar: Optional[int] = Field(default=None, ge=1)
    kategoria: Optional[str] = None
    keszlet: Optional[int] = Field(default=None, ge=0)
    aktiv: Optional[bool] = None


class FelhasznaloCreate(BaseModel):
    felhasznalonev: str = Field(min_length=3)
    jelszo: str = Field(min_length=6)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
