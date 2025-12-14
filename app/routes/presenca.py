from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config.config import SessionLocal
from app.models import Presenca
from app import schemas

router = APIRouter(prefix="/presencas", tags=["presencas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.PresencaOut)
def create_presenca(payload: schemas.PresencaCreate, db: Session = Depends(get_db)):
    p = Presenca(**payload.dict())
    db.add(p)
    db.commit()
    db.refresh(p)
    return p


@router.get("/", response_model=List[schemas.PresencaOut])
def list_presencas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Presenca).offset(skip).limit(limit).all()


@router.get("/{presenca_id}", response_model=schemas.PresencaOut)
def get_presenca(presenca_id: int, db: Session = Depends(get_db)):
    p = db.get(Presenca, presenca_id)
    if not p:
        raise HTTPException(status_code=404, detail="Presenca not found")
    return p


@router.put("/{presenca_id}", response_model=schemas.PresencaOut)
def update_presenca(presenca_id: int, payload: schemas.PresencaCreate, db: Session = Depends(get_db)):
    p = db.get(Presenca, presenca_id)
    if not p:
        raise HTTPException(status_code=404, detail="Presenca not found")
    for k, v in payload.dict().items():
        setattr(p, k, v)
    db.add(p)
    db.commit()
    db.refresh(p)
    return p


@router.delete("/{presenca_id}")
def delete_presenca(presenca_id: int, db: Session = Depends(get_db)):
    p = db.get(Presenca, presenca_id)
    if not p:
        raise HTTPException(status_code=404, detail="Presenca not found")
    db.delete(p)
    db.commit()
    return {"ok": True}
