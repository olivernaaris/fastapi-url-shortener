from pydantic import BaseModel

# Pydantic models


class Url(BaseModel):
    url: str
