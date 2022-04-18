from typing import Type

from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticClient
from motor.core import Database
from typing import Type

def get_db() -> Type[Database] :
    client: AgnosticClient = AsyncIOMotorClient()
    db: Database = client["todos-fastapi"]
    client
    assert  db.name == "todos-fastapi"
    return db

def close_db(client: AgnosticClient):
    client.close()
    