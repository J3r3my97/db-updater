from dateutil.relativedelta import *
from sqlalchemy.orm import Session

import models
import schemas


def get_all_patients(db: Session):
    return db.query(models.Patient).all()


def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(
        fname=patient.fname,
        lname=patient.lname,
        email=patient.email,
        dob=patient.dob,
        address=patient.address,
        state=patient.state,
        gender=patient.gender,
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient
