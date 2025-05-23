from typing import Optional
from pydantic import BaseModel # type: ignore
from sqlmodel import Field, SQLModel

class Customer(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    name:str
    email:str

class customer_input(BaseModel):
    name:str
    email:str