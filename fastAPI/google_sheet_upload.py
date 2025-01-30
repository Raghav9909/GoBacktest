import os
import pandas as pd
import google.auth
from googleapiclient.discovery import build

def authenticate():
    """
    Authenticates using Application Default Credentials.
    """
    creds, _ = google.auth.default()
    return creds

def create_sheet(title):
    """
    Creates a Google Spreadsheet and returns the spreadsheet ID.
    """
    creds = authenticate()
    service = build("sheets", "v4", credentials=creds)

    spreadsheet = {"properties": {"title": title}}
    
    try:
        spreadsheet = service.spreadsheets().create(
            body=spreadsheet, fields="spreadsheetId"
        ).execute()
        print(f"Spreadsheet ID: {spreadsheet.get('spreadsheetId')}")
        return spreadsheet.get("spreadsheetId")
    except Exception as error:
        print(f"An error occurred: {error}")
        return None

def load_csv_to_sheet(spreadsheet_id, csv_file_path, sheet_name="Sheet1"):
    """
    Reads a CSV file and uploads the data to a Google Spreadsheet.
    """
    creds = authenticate()
    service = build("sheets", "v4", credentials=creds)

    # Read CSV into Pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Convert DataFrame to list of lists
    values = [df.columns.tolist()] + df.values.tolist()
    
    body = {"values": values}

    try:
        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=f"{sheet_name}!A1",
            valueInputOption="RAW",
            body=body
        ).execute()
        print(f"CSV data uploaded to spreadsheet: {spreadsheet_id}")
    except Exception as error:
        print(f"An error occurred: {error}")

def upload_sheet(csv_file,sheet_name):
    spreadsheet_id = create_sheet(sheet_name)
    load_csv_to_sheet(spreadsheet_id, csv_file)

if __name__ == "__main__":
    csv_file = "TSLA_backtest.csv"  # Change this to your CSV file path
    spreadsheet_id = create_sheet("Dataset")

    if spreadsheet_id:
        load_csv_to_sheet(spreadsheet_id, csv_file)
