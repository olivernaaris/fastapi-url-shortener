from sqlalchemy.orm import Session

from app.models import models


def create_short_url(db: Session, original_url: str, short_url: str):
    db_url = models.Url(original_url=original_url, short_url=short_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url


def get_original_url(db: Session, original_url: str):
    return db.query(models.Url.original_url).filter(models.Url.original_url == original_url).first()


def get_short_url(db: Session, short_url: str):
    return db.query(models.Url.short_url).filter(models.Url.short_url == short_url).first()


def get_urls_list(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Url).offset(skip).limit(limit).all()


def find_original_url_by_short_url(db: Session, short_url: str):
    return db.query(models.Url.original_url).filter(models.Url.short_url == short_url).first()
