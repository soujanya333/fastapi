from datetime import datetime, date
from pydantic import BaseModel


class UserLog(BaseModel):
    firstname: str
    lastname: str
    email: str
    mobile_no:str