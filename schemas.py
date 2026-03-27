from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str
    owner: str

class TaskUpdate(BaseModel):
    title: str = None
    description: str = None
    status: str = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    owner: str

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

