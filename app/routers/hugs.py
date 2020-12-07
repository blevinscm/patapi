from fastapi import APIRouter, HTTPException
from ..data import models
from typing import List
from odmantic import AIOEngine, ObjectId
from motor.motor_asyncio import AsyncIOMotorClient
import os

router = APIRouter()
URI = 'mongodb://pat-mongo:hkFhaUPLqi52ZpHpOpzrHhrLvE2efpEwg0MBRSBYVcYgPZYVkztFb8bfvbpRqZdcT1SqjdZqUmMcJp0UTfTrtg==@pat-mongo.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@pat-mongo@'

Hug = models.Hug
client = AsyncIOMotorClient(URI)
engine = AIOEngine(motor_client=client)

@router.put("/hugs/", response_model=Hug, tags=["hugs"])
async def new_hug(hug: Hug):
    '''
    Add a hug to the Database.
    Delete the objectID from the example if using 
    swaggerUI
    Use to add or edit an item in the DB. Do not use Post
    when using MongoDB.
    '''
    await engine.save(hug)
    return hug


@router.get("/hugs/", response_model=List[Hug], tags=["hugs"])
async def get_hugs():
    '''
    Get all the hugs from the database.
    Used to get a list of the items in the database.
    '''
    hugs = await engine.find(Hug)
    return hugs


@router.get("/hugs/count", response_model=int, tags=["hugs"])
async def count_hugs():
    '''
    Count all the hugs in the database.
    Useful for determining pagination, optimizations.
    '''
    count = await engine.count(Hug)
    return count


@router.get("/hugs/{id}", response_model=Hug, tags=["hugs"])
async def get_hug_by_id(id: ObjectId):
    '''
    Find a specific hug by ID.
    '''
    hug = await engine.find_one(Hug, Hug.id == id)
    if hug is None:
        raise HTTPException(404)
    return hug