from fastapi import FastAPI
from .database import Base, engine
from .routers import public, private

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="URL Shortener",
    docs_url="/docs"
)

app.include_router(public.router)
app.include_router(private.router, prefix="/admin")
