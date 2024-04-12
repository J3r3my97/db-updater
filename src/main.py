import logging


import uvicorn
from fastapi import Depends, FastAPI
import database
import models
import crud
from sqlalchemy.orm import Session

# Custom logger configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)



app = FastAPI(
    title="Dental-Analytic-API",
)

# models.database.Base.metadata.create_all(bind=database.engine)



# Dependency
# def get_db():
#     db = database.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


@app.get("/health", tags=["health_check"])
async def root():
    return {"message": "app is running"}


# @app.get("/patients", tags=["patients"])
# async def get_patients(db: Session = Depends(get_db)):
#     patients = crud.get_all_patients(db)
#     return patients


# TODO: add a router for inserting a single patient
# @app.post("/patients", tags=["patients"])
# async def create_patient(patient: models.PatientCreate, db: Session = Depends(get_db)):
#     return crud.create_patient(db, patient)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
