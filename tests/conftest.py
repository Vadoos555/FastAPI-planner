import asyncio
import httpx
import pytest

from database.connection import Settings
from main import app
from models.events import Event
from models.users import User


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()


async def init_db():
    test_settings = Settings()
    test_settings.DATABASE_NAME = "test_db"
    
    await test_settings.initialize_db()


@pytest.fixture(scope='session')
async def default_client():
    await init_db()
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url='http://app') as client:
        yield client
        
        # clean up resouces
        await Event.find_all().delete()
        await User.find_all().delete()
        