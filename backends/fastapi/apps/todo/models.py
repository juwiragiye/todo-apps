import uuid
from typing import Optional


from pydantic import BaseModel, Field


class TaskModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id") # give alias to be rec by mongo db
    desc: str = Field(...)
    completed: bool = False

    class Config:
        allow_population_by_field_name = True 
        schema_extra = {
            "example": {
                "id": "35c28bcf-e818-4388-bc20-45e8719e0c76",
                "desc": "finish the whole api",
                "completed": False
            }
        }


class UpdateTask(BaseModel):
    desc: Optional[str]
    completed: Optional[bool]

    class Config:
                schema_extra = {
            "example": {
                "desc": "wrtie a good readme.md",
                "completed": True,
            }
        }