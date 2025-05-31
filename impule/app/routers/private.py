from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud, schemas
from ..auth import get_current_username

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create", response_model=schemas.URLInfo)
def create_url(url: schemas.URLCreate, db: Session = Depends(get_db), user: str = Depends(get_current_username)):
    db_url = crud.create_short_url(db, url.orig_link, url.expire_days)
    return {
        "link": f"http://localhost:8000/{db_url.short}",
        "orig_link": db_url.original,
        "last_hour_clicks": 0,
        "last_day_clicks": 0
    }
