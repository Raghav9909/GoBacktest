from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Path to the CSV file
CSV_FILE_PATH = "/TSLA_backtest.csv"

# Google Sheets credentials
GOOGLE_SHEETS_CREDENTIALS_FILE = "google_credentials.json"
GOOGLE_SHEET_NAME = "Backtest"
GOOGLE_SHEET_TAB_NAME = "Sheet1"  # Name of the tab in the Google Sheet

# Function to upload CSV to Google Sheets
# def upload_csv_to_google_sheets():
#     # Authenticate with Google Sheets
#     scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
#     creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_SHEETS_CREDENTIALS_FILE, scope)
#     client = gspread.authorize(creds)

#     # Open the Google Sheet
#     sheet = client.open(GOOGLE_SHEET_NAME).worksheet(GOOGLE_SHEET_TAB_NAME)

#     # Read the CSV file
#     df = pd.read_csv(CSV_FILE_PATH)

#     # Clear the existing sheet content
#     sheet.clear()

#     # Upload the DataFrame to Google Sheets
#     sheet.update([df.columns.values.tolist()] + df.values.tolist())

#     print(f"CSV file {CSV_FILE_PATH} uploaded to Google Sheets.")

# # Define the DAG
# default_args = {
#     'owner': 'airflow',
#     'start_date': days_ago(1),
#     'retries': 1,
# }

# dag = DAG(
#     'csv_to_google_sheets_instant',
#     default_args=default_args,
#     description='A DAG to upload a CSV file to Google Sheets instantly',
#     schedule_interval=None,  # No schedule, trigger manually
#     catchup=False,
# )

# # Task to upload the CSV to Google Sheets
# upload_task = PythonOperator(
#     task_id='upload_csv_to_google_sheets',
#     python_callable=upload_csv_to_google_sheets,
#     dag=dag,
# )

# # Define the workflow
# upload_task

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def create(title):
  """
  Creates the Sheet the user has access to.
  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """
  creds, _ = google.auth.default()
  # pylint: disable=maybe-no-member
  try:
    service = build("sheets", "v4", credentials=creds)
    spreadsheet = {"properties": {"title": title}}
    spreadsheet = (
        service.spreadsheets()
        .create(body=spreadsheet, fields="spreadsheetId")
        .execute()
    )
    print(f"Spreadsheet ID: {(spreadsheet.get('spreadsheetId'))}")
    return spreadsheet.get("spreadsheetId")
  except HttpError as error:
    print(f"An error occurred: {error}")
    return error


if __name__ == "__main__":
  # Pass: title
  create("dataset")