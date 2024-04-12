import pandas as pd
from google.cloud import storage
from io import BytesIO
from db import connect_with_connector
import logging
import base64
import json


conn = connect_with_connector()
logger = logging.getLogger

def load_df_into_database(df, table_name="patients"):
    try:
        result = df.to_sql(table_name, conn, if_exists="append", index=False)
        print(result)
        print("load_df_into_database() done: result = ", result)
    except Exception as e:
        print("load_df_into_database() error: ", e)

def load_csv_from_gcs(bucket_name, blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    content = blob.download_as_string()
    df = pd.read_csv(BytesIO(content))
    return df

def handle_triggering_events(event, context):
    try:
        json_payload = base64.b64decode(event['datat'])
        data_payload = json.loads(json_payload)
        bucket_name = data_payload['bucket_name']
        blob_name = data_payload['blob_name']
        logger.info(f"received payload, processing csv file from {bucket_name}/{blob_name}")
        df = load_csv_from_gcs(bucket_name, blob_name)
        load_df_into_database(df, table_name="patients")
    except Exception as e:
        print(f"error handling event {event} error: {e}")