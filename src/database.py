import os
from typing import Generator

import google.auth
from google.cloud.sql.connector import Connector, IPTypes
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = os.environ.get("DB_USER", "oa-intern")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
DB_HOST = os.environ.get("DB_HOST", "calcium-backup-338422:us-central1:dental-analytic-db")
DB_PORT = os.environ.get("DB_PORT", 5432)
DB_NAME = os.environ.get("DB_NAME", "postgres")
ENV = os.environ.get("ENV", "cloud")

Base = declarative_base()


def init_connection_engine(connector: Connector) -> Engine:
    """
    Initializes a connection pool for a Cloud SQL instance of Postgres.

    Uses the Cloud SQL Python Connector with Automatic IAM Database Authentication.
    """
    instance_connection_name = os.environ["DB_HOST"]
    db_iam_user = os.environ["DB_USER"]
    db_name = os.environ["DB_NAME"]

    ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC

    # grab sa token
    creds, project = google.auth.default()

    if creds.expired:
        auth_req = google.auth.transport.requests.Request()
        creds.refresh(auth_req)

    db_password = creds.token

    def getconn():
        conn = connector.connect(
            instance_connection_name,
            "pg8000",
            user=db_iam_user,
            db=db_name,
            password=db_password,
            enable_iam_auth=True,
            ip_type=ip_type,
        )
        return conn

    engine = create_engine(
        "postgresql+pg8000://",
        creator=getconn,
    )

    return engine


if ENV == "local":
    DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    print(f"connecting to {DB_URL}")
    engine = create_engine(DB_URL)

else:
    print("connecting to cloud sql")
    print(f"debug: connecting to {DB_HOST}")
    print(f"debug: connecting with {DB_USER}")
    connector = Connector()
    engine = init_connection_engine(connector)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
