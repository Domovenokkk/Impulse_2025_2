from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from .database import Base

class ShortURL(Base):
    __tablename__ = "short_urls"
    id = Column(Integer, primary_key=True, index=True)
    short = Column(String, unique=True, index=True)
    original = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime)
    clicks = Column(Integer, default=0)
