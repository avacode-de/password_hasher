from pydantic_settings import BaseModel

class UserCreate(BaseModel):
    user_name: str
    password: str