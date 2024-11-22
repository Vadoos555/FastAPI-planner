from pydantic import BaseModel
from beanie import Document


class Event(Document):
    creator: str | None = None
    title: str
    image: str
    description: str
    tags: list[str]
    location: str
    
    class Settings:
        name = 'events'


class EventUpdate(BaseModel):
    title: str | None = None
    image: str | None = None
    description: list[str] | None = None
    location: str | None = None
    