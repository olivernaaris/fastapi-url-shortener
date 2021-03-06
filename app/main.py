from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models import models
from app.schemas import schema
from . import crud
from .database import SessionLocal, engine

import shortuuid

SERVER_DOMAIN = 'http://127.0.0.1:8000'

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
def welcome():
    return {'message': 'Welcome to Url shortener app.'}


@app.get("/list")
def get_urls_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_url_list = crud.get_urls_list(db, skip=skip, limit=limit)
    return {'message': db_url_list}


@app.get("/{short_url}")
def get_original_url(short_url: str, db: Session = Depends(get_db)):
    db_original_url = crud.find_original_url_by_short_url(db=db, short_url=str(f'{SERVER_DOMAIN}/{short_url}'))
    return db_original_url[0]


@app.post("/shorten")
def create_short_url(req: schema.Url, db: Session = Depends(get_db)):
    original_url = req.url
    db_both_urls = crud.get_both_urls(db=db, original_url=original_url)
    if db_both_urls:
        return {'message': f'{db_both_urls.original_url} is already shortened -- short Url is {db_both_urls.short_url}'}
    short_url = f'{SERVER_DOMAIN}/{shortuuid.uuid(name=original_url)[:8]}'
    crud.create_short_url(db=db, original_url=original_url, short_url=short_url)
    return {'message': f'Url you want to shorten is {original_url} -- I created a short Url for you {short_url}'}
