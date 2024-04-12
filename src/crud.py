from dateutil.relativedelta import *
from sqlalchemy.orm import Session
import models


def get_all_patients(db: Session):
    return db.query(models.Patient).all()
