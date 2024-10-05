from prefect import task, flow
from minio import Minio
from pymongo import MongoClient
import pandas as pd
from io import BytesIO

# MinIO client configuration
minio_client = Minio(
    "minio:9000",
    access_key="your-access-key",
    secret_key="your-secret-key",
    secure=False
)

# MongoDB client configuration
mongo_client = MongoClient("mongodb://mongo:27017/")
db = mongo_client["your_database"]
collection = db["your_collection"]

@task
def extract_from_minio(bucket_name, object_name):
    response = minio_client.get_object(bucket_name, object_name)
    data = response.read()
    df = pd.read_csv(BytesIO(data))
    return df

@task
def transform_data(df):
    # Perform any data transformation here
    #  df['new_column'] = df['existing_column'] * 2  # Example transformation
    return df

@task
def load_to_mongodb(df):
    records = df.to_dict(orient='records')
    collection.insert_many(records)

@flow
def etl_pipeline():
    bucket_name = "your-bucket-name"
    object_name = "alphabot_000000_2024_05_20_18_37_11-data.csv"
    df = extract_from_minio(bucket_name, object_name)
    transformed_df = transform_data(df)
    load_to_mongodb(transformed_df)

if __name__ == "__main__":
    etl_pipeline()
