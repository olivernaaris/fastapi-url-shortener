from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from app.database import Base


class UrlModel(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, index=True)
    short_url = Column(String, index=True)