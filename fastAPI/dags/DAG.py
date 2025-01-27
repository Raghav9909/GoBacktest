from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import requests
import json
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# Google Sheets setup
SHEET_ID = "your_google_sheet_id"
RANGE_NAME = "Sheet1!A1"  # Adjust based on your sheet structure
SERVICE_ACCOUNT_FILE = "/path/to/your-service-account.json"

def fetch_data_from_fastapi():
    url = "http://your-fastapi-endpoint/data"  # Replace with your FastAPI endpoint
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def populate_google_sheet(**context):
    # Fetch data from FastAPI task
    data = context['ti'].xcom_pull(task_ids='fetch_data')

    # Prepare data for Google Sheets (list of lists format)
    sheet_data = [["Name", "Age"]]  # Header
    for row in data:
        sheet_data.append([row["name"], row["age"]])

    # Authenticate with Google Sheets API
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()

    # Update the Google Sheet
    body = {"values": sheet_data}
    sheet.values().update(
        spreadsheetId=SHEET_ID,
        range=RANGE_NAME,
        valueInputOption="RAW",
        body=body
    ).execute()

# Define the Airflow DAG
with DAG(
    dag_id="populate_google_sheet",
    default_args={"owner": "airflow", "retries": 1},
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
) as dag:
    fetch_data = PythonOperator(
        task_id="fetch_data",
        python_callable=fetch_data_from_fastapi,
    )

    update_sheet = PythonOperator(
        task_id="update_google_sheet",
        python_callable=populate_google_sheet,
        provide_context=True,
    )

    fetch_data >> update_sheet
