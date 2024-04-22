from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PatientBase(BaseModel):
    id: Optional[int] = None
    fname: str
    lname: str
    email: str
    gender: str
    address: str
    dob: datetime
    state: str


class PatientCreate(PatientBase):
    pass
