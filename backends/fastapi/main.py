import imp
import uvicorn
from fastapi import FastAPI


from motor.motor_asyncio import AsyncIOMotorClient

from config import settings

app = FastAPI()


@app.on_event("startup")
async def startup_db_client():
    # app.mongodb_client = AsyncIOMotorClient(settings.DB_URL)
    # app.mongodb = app.mongodb_client[settings.DB_NAME]
    """
    Start the mongo db database before the app loads up. Customize the settings of your dabatase here.
    """
    
    mongo_client = AsyncIOMotorClient()
    mongdb = mongo_client["todos-fastapi"]
    app.mongodb_client = mongo_client
    app.mongodb = mongdb
    
  


@app.on_event("shutdown")
async def shutdown_db_client():
  
    assert app.mongodb_client
   # assert here I'm not sure
    app.mongodb_client.close()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        # host=settings.HOST,
        # reload=settings.DEBUG_MODE,
        # port=settings.PORT,
        reload=True
    )