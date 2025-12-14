from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config.config import SessionLocal
from app.models import Equipe
from app import schemas

router = APIRouter(prefix="/equipes", tags=["equipes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.EquipeOut)
def create_equipe(payload: schemas.EquipeCreate, db: Session = Depends(get_db)):
    e = Equipe(**payload.dict())
    db.add(e)
    db.commit()
    db.refresh(e)
    return e


@router.get("/", response_model=List[schemas.EquipeOut])
def list_equipes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Equipe).offset(skip).limit(limit).all()


@router.get("/{equipe_id}", response_model=schemas.EquipeOut)
def get_equipe(equipe_id: int, db: Session = Depends(get_db)):
    e = db.get(Equipe, equipe_id)
    if not e:
        raise HTTPException(status_code=404, detail="Equipe not found")
    return e


@router.put("/{equipe_id}", response_model=schemas.EquipeOut)
def update_equipe(equipe_id: int, payload: schemas.EquipeCreate, db: Session = Depends(get_db)):
    e = db.get(Equipe, equipe_id)
    if not e:
        raise HTTPException(status_code=404, detail="Equipe not found")
    for k, v in payload.dict().items():
        setattr(e, k, v)
    db.add(e)
    db.commit()
    db.refresh(e)
    return e


@router.delete("/{equipe_id}")
def delete_equipe(equipe_id: int, db: Session = Depends(get_db)):
    e = db.get(Equipe, equipe_id)
    if not e:
        raise HTTPException(status_code=404, detail="Equipe not found")
    db.delete(e)
    db.commit()
    return {"ok": True}
