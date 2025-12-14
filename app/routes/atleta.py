from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config.config import SessionLocal
from app.models import Atleta
from app import schemas

router = APIRouter(prefix="/atletas", tags=["atletas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.AtletaOut)
def create_atleta(payload: schemas.AtletaCreate, db: Session = Depends(get_db)):
    a = Atleta(**payload.dict())
    db.add(a)
    db.commit()
    db.refresh(a)
    return a


@router.get("/", response_model=List[schemas.AtletaOut])
def list_atletas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Atleta).offset(skip).limit(limit).all()


@router.get("/{atleta_id}", response_model=schemas.AtletaOut)
def get_atleta(atleta_id: int, db: Session = Depends(get_db)):
    a = db.get(Atleta, atleta_id)
    if not a:
        raise HTTPException(status_code=404, detail="Atleta not found")
    return a


@router.put("/{atleta_id}", response_model=schemas.AtletaOut)
def update_atleta(atleta_id: int, payload: schemas.AtletaCreate, db: Session = Depends(get_db)):
    a = db.get(Atleta, atleta_id)
    if not a:
        raise HTTPException(status_code=404, detail="Atleta not found")
    for k, v in payload.dict().items():
        setattr(a, k, v)
    db.add(a)
    db.commit()
    db.refresh(a)
    return a


@router.delete("/{atleta_id}")
def delete_atleta(atleta_id: int, db: Session = Depends(get_db)):
    a = db.get(Atleta, atleta_id)
    if not a:
        raise HTTPException(status_code=404, detail="Atleta not found")
    db.delete(a)
    db.commit()
    return {"ok": True}
