from dateutil.relativedelta import *
from sqlalchemy import insert
from sqlalchemy.orm import Session
import models


def get_all_patients(db: Session):
    return db.query(models.Patient).all()

def create_patient(db: Session):
    patient = models.Patient(fname="John", lname="Doe", email="johndoe@example.com", gender="Male", dob="1990-01-01", address="123 Main St", state="CA")
    db.add(patient)
    db.commit()
    return "Patient is created!"
