from sqlalchemy.orm import Session
from . import models
from datetime import datetime, timedelta
import string, random

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def create_short_url(db: Session, orig_url: str, expire_days: int = 1):
    short = generate_short_url()
    expires_at = datetime.utcnow() + timedelta(days=expire_days)
    db_obj = models.ShortURL(short=short, original=orig_url, expires_at=expires_at)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_original_url(db: Session, short: str):
    return db.query(models.ShortURL).filter_by(short=short, is_active=True).first()
