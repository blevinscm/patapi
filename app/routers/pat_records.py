from fastapi import APIRouter, HTTPException
from ..data import models
from typing import List
from odmantic import AIOEngine, ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

router = APIRouter()
URI = 'mongodb://pat-mongo:hkFhaUPLqi52ZpHpOpzrHhrLvE2efpEwg0MBRSBYVcYgPZYVkztFb8bfvbpRqZdcT1SqjdZqUmMcJp0UTfTrtg==@pat-mongo.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@pat-mongo@'

Record = models.Record
client = AsyncIOMotorClient(URI)
engine = AIOEngine(motor_client=client, database="pat_records")

@router.put("/record/", response_model=Record, tags=["Record Add"])
async def new_record(record: Record):
    '''
    Add a record to the Database.
    Delete the objectID from the example if using 
    swaggerUI
    Use to add or edit an item in the DB. Do not use Post
    when using MongoDB.
    '''
    await engine.save(record)
    return record


@router.get("/records/", response_model=List[Record], tags=["Record Retrieval"])
async def get_records():
    '''
    Get all the records from the database.
    Used to get a list of the items in the database.
    '''
    records = await engine.find(Record)
    return records


@router.get("/records/count", response_model=int, tags=["Record Retrieval"])
async def count_records():
    '''
    Count all the records in the database.
    Useful for determining pagination, optimizations.
    '''
    count = await engine.count(Record)
    return count


@router.get("/records/{id}", response_model=Record, tags=["Record Retrieval"])
async def get_record_by_id(id: ObjectId):
    '''
    Find a specific record by ID.
    '''
    record = await engine.find_one(Record, Record.id == id)
    if record is None:
        raise HTTPException(404)
    return record