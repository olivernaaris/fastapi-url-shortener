from sqlalchemy.orm import Session
from typing import List

from app.models import models


def get_both_urls(db: Session, original_url: str) -> "UrlModel":
    return db.query(models.UrlModel).filter(models.UrlModel.original_url == original_url).first()


def get_urls_list(db: Session, skip: int = 0, limit: int = 100) -> List["UrlModel"]:
    return db.query(models.UrlModel).offset(skip).limit(limit).all()


def find_original_url_by_short_url(db: Session, short_url: str) -> List[str]:
    return db.query(models.UrlModel.original_url).filter(models.UrlModel.short_url == short_url).first()


def create_short_url(db: Session, original_url: str, short_url: str):
    db_url = models.UrlModel(original_url=original_url, short_url=short_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url
