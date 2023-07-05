from pydantic import BaseModel, Field


class Character(BaseModel):
    name: str
