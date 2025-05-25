import requests
from google.cloud import storage
from datetime import datetime
import os

BUCKET_NAME = os.environ.get("tlc_historicos")
CSV_URL = os.environ.get("https://data.cityofnewyork.us/resource/t29m-gskq.csv")

def main():
    try:
        response = requests.get(CSV_URL)
        response.raise_for_status()

        filename = f"archivo_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.csv"

        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)
        blob = bucket.blob(filename)
        blob.upload_from_string(response.content, content_type='text/csv')

        print(f"✅ Archivo subido: {filename}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()

