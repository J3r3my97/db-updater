import os

from google.cloud.sql.connector import Connector


from sqlalchemy import create_engine


def connect_with_connector():
    """
    Initializes a connection pool for a Cloud SQL instance of Postgres.

    Uses the Cloud SQL Python Connector package.
    """
    # Note: Saving credentials in environment variables is convenient, but not
    # secure - consider a more secure solution such as
    # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    # keep secrets safe.

    instance_connection_name = 'calcium-backup-338422:us-central1:dental-analytic-db'
    db_user = 'oa-intern'  # e.g. 'my-db-user'
    db_pass = 'oa2023'  # e.g. 'my-db-password'
    db_name = 'postgres'  # e.g. 'my-database'


    # initialize Cloud SQL Python Connector object
    connector = Connector()

    def getconn():
        conn = connector.connect(
            instance_connection_name,
            "pg8000",
            user=db_user,
            password=db_pass,
            db=db_name,
        )
        return conn

    # The Cloud SQL Python Connector can be used with SQLAlchemy
    # using the 'creator' argument to 'create_engine'
    engine = create_engine(
        "postgresql+pg8000://",
        creator=getconn,
    )
    return engine