from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..crud import get_original_url
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{short}")
def redirect_short_url(short: str, db: Session = Depends(get_db)):
    db_url = get_original_url(db, short)
    if not db_url or db_url.expires_at < datetime.utcnow():
        raise HTTPException(status_code=404, detail="URL not found or expired")
    db_url.clicks += 1
    db.commit()
    return {"original": db_url.original}
