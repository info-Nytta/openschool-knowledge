from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from database import get_db
from models import FelhasznaloModel
from schemas import FelhasznaloCreate

SECRET_KEY = "vizsga2026"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/regisztracio", status_code=201)
def regisztracio(felhasznalo: FelhasznaloCreate, db: Session = Depends(get_db)):
    letezo = db.query(FelhasznaloModel).filter(
        FelhasznaloModel.felhasznalonev == felhasznalo.felhasznalonev
    ).first()
    if letezo:
        raise HTTPException(status_code=400, detail="Felhasználónév foglalt")
    jelszo_hash = pwd_context.hash(felhasznalo.jelszo)
    uj = FelhasznaloModel(
        felhasznalonev=felhasznalo.felhasznalonev,
        jelszo_hash=jelszo_hash,
    )
    db.add(uj)
    db.commit()
    return {"message": "Sikeres regisztráció"}


@router.post("/login")
def login(felhasznalo: FelhasznaloCreate, db: Session = Depends(get_db)):
    user = db.query(FelhasznaloModel).filter(
        FelhasznaloModel.felhasznalonev == felhasznalo.felhasznalonev
    ).first()
    if not user or not pwd_context.verify(felhasznalo.jelszo, user.jelszo_hash):
        raise HTTPException(status_code=401, detail="Hibás bejelentkezési adatok")
    token = jwt.encode({"sub": user.felhasznalonev}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        felhasznalonev = payload.get("sub")
        if felhasznalonev is None:
            raise HTTPException(status_code=401, detail="Érvénytelen token")
        return felhasznalonev
    except JWTError:
        raise HTTPException(status_code=401, detail="Érvénytelen token")
