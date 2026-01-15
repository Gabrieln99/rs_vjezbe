from pydantic import BaseModel

class Actor(BaseModel):
    name: str
    surname: str

class Writer(BaseModel):
    name: str
    surname: str
