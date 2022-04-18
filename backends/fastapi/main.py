import uvicorn
from fastapi import FastAPI


from database import get_db, close_db

app = FastAPI()


@app.on_event("startup")
def startup_db_client():
  
    """
    Start the mongo db database before the app loads up. Customize the settings of your dabatase here.
    """
    # Handle for when the excepet is baa
    db = get_db()

@app.on_event("shutdown")
async def shutdown_db_client():
    close_db()


if __name__ == "__main__":
   
    print(startup_db_client())
    uvicorn.run(
        "main:app",
    
        reload=True # TODO: Make sure false for production
    )