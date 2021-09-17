from pydantic import BaseModel

class Model(BaseModel):
    user: str
    passwd :str