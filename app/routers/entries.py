from fastapi import APIRouter, HTTPException
from ..data import models
from typing import List
from odmantic import AIOEngine, ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

router = APIRouter()
URI = 'mongodb://pat-mongo:hkFhaUPLqi52ZpHpOpzrHhrLvE2efpEwg0MBRSBYVcYgPZYVkztFb8bfvbpRqZdcT1SqjdZqUmMcJp0UTfTrtg==@pat-mongo.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@pat-mongo@'

Entry = models.Entry
client = AsyncIOMotorClient(URI)
engine = AIOEngine(motor_client=client, database="pat_entries")

@router.put("/entry/", response_model=Entry, tags=["Entry Add/Edit"])
async def new_entry(entry: Entry):
    '''
    Add a record to the Database.
    Delete the objectID from the example if using 
    swaggerUI
    Use to add or edit an item in the DB. Do not use Post
    when using MongoDB.
    '''
    await engine.save(entry)
    return entry


@router.get("/entries/", response_model=List[Entry], tags=["Entry Retrieval"])
async def get_entries():
    '''
    Get all the entries from the database.
    Used to get a list of the items in the database.
    '''
    entries = await engine.find(Entry)
    return entries


@router.get("/entries/count", response_model=int, tags=["Entry Retrieval"])
async def count_entries():
    '''
    Count all the records in the database.
    Useful for determining pagination, optimizations.
    '''
    count = await engine.count(Entry)
    return count


@router.get("/entries/{id}", response_model=Entry, tags=["Entry Retrieval"])
async def get_entry_by_id(id: ObjectId):
    '''
    Find a specific record by ID.
    '''
    entry = await engine.find_one(Entry, Entry.id == id)
    if entry is None:
        raise HTTPException(404)
    return entry