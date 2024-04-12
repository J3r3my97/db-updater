from datetime import datetime
from pydantic import BaseModel


class PatientBase(BaseModel):
    id: int
    fanme: str
    lname: str
    email: str
    gender: str
    address: str
    dob: datetime
    state: str
