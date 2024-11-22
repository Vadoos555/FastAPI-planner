import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from database.connection import Settings
from routes.users import user_router
from routes.events import event_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await settings.initialize_db()
    yield


app = FastAPI(lifespan=lifespan)

settings = Settings()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


@app.get('')
async def home():
    return RedirectResponse(url='/event/')


if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=8000, reload=True)
