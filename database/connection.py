import os

from beanie import init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from typing import Any
from dotenv import load_dotenv


from models.events import Event
from models.users import User


load_dotenv()


class Settings(BaseModel):
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME") 
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    
    async def initialize_db(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        database = client[self.DATABASE_NAME]
        await init_beanie(
            database=database,
            document_models=[Event, User]
        )


class DataBase:
    def __init__(self, model) -> None:
        self.model = model
    
    async def save(self, document) -> None:
        await document.create()
        return
    
    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False
    
    async def get_all(self) -> list[Any]:
        docs = await self.model.find_all().to_list()
        return docs
    
    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.model.get(id)
        if not doc:
            return False
        await doc.delete()
        return True
    
    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc_id = id
        des_body = body.model_dump(exclude_unset=True)
        
        update_query = {
            "$set": { k: v for k, v in des_body.items()}
        }
        
        doc = await self.model.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc
    