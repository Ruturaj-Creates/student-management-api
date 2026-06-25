from pydantic import BaseModel,EmailStr,Field


class StudentCreate(BaseModel):
    name: str=Field(min_length=1)
    age: int=Field(gt=0)
    email: EmailStr

class StudentResponse(BaseModel):
    id:int
    name: str=Field(min_length=1)
    age: int=Field(gt=0)
    email: EmailStr

class StudentUpdate(BaseModel):
    name:str|None=Field(min_length=1,default=None)
    age:int|None=Field(gt=0,default=None)
    email:EmailStr|None=Field(default=None)