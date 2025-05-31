from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional

class URLCreate(BaseModel):
    orig_link: HttpUrl
    expire_days: Optional[int] = 1

class URLInfo(BaseModel):
    link: str
    orig_link: HttpUrl
    last_hour_clicks: int
    last_day_clicks: int
