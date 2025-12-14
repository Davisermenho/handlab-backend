from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config.config import SessionLocal
from app.models import Usuario
from app import schemas

router = APIRouter(prefix="/usuarios", tags=["usuarios"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.UsuarioOut)
def create_usuario(payload: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = Usuario(**payload.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


@router.get("/", response_model=List[schemas.UsuarioOut])
def list_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Usuario).offset(skip).limit(limit).all()


@router.get("/{usuario_id}", response_model=schemas.UsuarioOut)
def get_usuario(usuario_id: int, db: Session = Depends(get_db)):
    u = db.get(Usuario, usuario_id)
    if not u:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return u


@router.put("/{usuario_id}", response_model=schemas.UsuarioOut)
def update_usuario(usuario_id: int, payload: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    u = db.get(Usuario, usuario_id)
    if not u:
        raise HTTPException(status_code=404, detail="Usuario not found")
    for k, v in payload.dict().items():
        setattr(u, k, v)
    db.add(u)
    db.commit()
    db.refresh(u)
    return u


@router.delete("/{usuario_id}")
def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    u = db.get(Usuario, usuario_id)
    if not u:
        raise HTTPException(status_code=404, detail="Usuario not found")
    db.delete(u)
    db.commit()
    return {"ok": True}
