from fastapi import APIRouter, HTTPException, status, Depends
from beanie import PydanticObjectId

from database.connection import DataBase
from models.events import Event, EventUpdate
from auth.authenticate import authenticate


event_router = APIRouter(tags=["Events"],)

event_db = DataBase(Event)


@event_router.get('/')
async def retrieve_all_events() -> list[Event]:
    events = await event_db.get_all()
    return events


@event_router.get('/{id}')
async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await event_db.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Event with supplied ID does not exist')
        
    return event


@event_router.post('/new')
async def create_event(body: Event, user: str = Depends(authenticate)) -> dict:
    body.creator = user
    await event_db.save(body)
    return {'message': 'Event created successfully'}


@event_router.delete('/{id}')
async def delete_event(id: PydanticObjectId, user: str = Depends(authenticate)) -> dict:
    event = await event_db.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Event not found')
    if event.creator != user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Operation not allowed"
        )
    event = await event_db.delete(id)
    return {'message': 'Event deleted successfully.'}


@event_router.put('/{id}', response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate, user: str = Depends(authenticate)) -> Event:
    event = await event_db.get(id)
    if event.creator != user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Operation not allowed")
        
    updated_event = await event_db.update(id, body)
    if not updated_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Event with supplied ID does not exist')
    
    return updated_event
    