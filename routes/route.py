from fastapi import APIRouter
from models.task import Task
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


@router.get('/tasks')
async def list_task():
    tasks = list_serial(collection_name.find())
    return tasks


@router.post('/tasks')
async def create_task(task: Task):
    collection_name.insert_one(dict(task))
    return task


@router.put('/tasks/{id}')
async def update_task(id: str, task: Task):
    collection_name.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(task)}
    )
    return task


@router.delete('/tasks/{id}')
async def destroy_task(id: str):
    collection_name.find_one_and_delete(
        {"_id": ObjectId(id)}
    )
    return {"message": "Task deleted"}
