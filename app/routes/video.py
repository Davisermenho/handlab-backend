from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config.config import SessionLocal
from app.models import Video
from app import schemas

router = APIRouter(prefix="/videos", tags=["videos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.VideoOut)
def create_video(payload: schemas.VideoCreate, db: Session = Depends(get_db)):
    v = Video(**payload.dict())
    db.add(v)
    db.commit()
    db.refresh(v)
    return v


@router.get("/", response_model=List[schemas.VideoOut])
def list_videos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Video).offset(skip).limit(limit).all()


@router.get("/{video_id}", response_model=schemas.VideoOut)
def get_video(video_id: int, db: Session = Depends(get_db)):
    v = db.get(Video, video_id)
    if not v:
        raise HTTPException(status_code=404, detail="Video not found")
    return v


@router.put("/{video_id}", response_model=schemas.VideoOut)
def update_video(video_id: int, payload: schemas.VideoCreate, db: Session = Depends(get_db)):
    v = db.get(Video, video_id)
    if not v:
        raise HTTPException(status_code=404, detail="Video not found")
    for k, val in payload.dict().items():
        setattr(v, k, val)
    db.add(v)
    db.commit()
    db.refresh(v)
    return v


@router.delete("/{video_id}")
def delete_video(video_id: int, db: Session = Depends(get_db)):
    v = db.get(Video, video_id)
    if not v:
        raise HTTPException(status_code=404, detail="Video not found")
    db.delete(v)
    db.commit()
    return {"ok": True}
