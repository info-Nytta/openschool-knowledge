from pydantic import BaseModel, Field
from typing import Optional


class PostCreate(BaseModel):
    cim: str = Field(min_length=5)
    tartalom: str = Field(min_length=10)
    szerzo: str = Field(min_length=3)
    cimke: Optional[str] = None


class PostRead(BaseModel):
    id: int
    cim: str
    tartalom: str
    szerzo: str
    cimke: Optional[str] = None
    publikalva: bool = False
    letrehozva: str

    class Config:
        from_attributes = True


class PostUpdate(BaseModel):
    cim: Optional[str] = None
    tartalom: Optional[str] = None
    cimke: Optional[str] = None
    publikalva: Optional[bool] = None


class FelhasznaloCreate(BaseModel):
    felhasznalonev: str = Field(min_length=3)
    jelszo: str = Field(min_length=6)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
