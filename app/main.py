from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models import models
from app.schemas import schema
from . import crud
from .database import SessionLocal, engine

import shortuuid

SERVER_DOMAIN = 'https://short-url.io'

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def shorten_url():
    return {'message': 'Welcome to Url shortener app.'}


@app.get("/list")
def get_urls_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_url_list = crud.get_urls_list(db, skip=skip, limit=limit)
    return {'message': db_url_list}


@app.post("/shorten")
def create_short_url(req: schema.Url, db: Session = Depends(get_db)):
    original_url = req.url
    db_original_url = crud.get_original_url(db=db, original_url=original_url)
    if db_original_url:
        return {'message': f'{original_url} is already shortened'}
    url_id = shortuuid.uuid(name=original_url)[:8]
    short_url = f'{SERVER_DOMAIN}/{url_id}'
    crud.create_short_url(db=db, original_url=original_url, short_url=short_url)
    return {'message': f'Url you want to shorten is {original_url} -- I created a short Url for you {short_url}'}
