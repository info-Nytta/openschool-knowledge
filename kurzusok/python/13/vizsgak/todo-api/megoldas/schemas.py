from pydantic import BaseModel, Field
from typing import Optional


class TodoCreate(BaseModel):
    cim: str = Field(min_length=3)
    leiras: Optional[str] = None
    prioritas: int = Field(default=3, ge=1, le=5)
    hatarido: Optional[str] = None


class TodoRead(BaseModel):
    id: int
    cim: str
    leiras: Optional[str] = None
    prioritas: int
    hatarido: Optional[str] = None
    kesz: bool = False
    letrehozva: str

    class Config:
        from_attributes = True


class TodoUpdate(BaseModel):
    cim: Optional[str] = None
    leiras: Optional[str] = None
    prioritas: Optional[int] = Field(default=None, ge=1, le=5)
    hatarido: Optional[str] = None
    kesz: Optional[bool] = None


class FelhasznaloCreate(BaseModel):
    felhasznalonev: str = Field(min_length=3)
    jelszo: str = Field(min_length=6)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
