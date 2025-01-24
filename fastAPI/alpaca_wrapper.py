import pandas as pd
from datetime import datetime, timedelta
import pytz

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
import pandas as pd
from datetime import datetime, timedelta
import pytz
from getpass import getpass

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from alpaca.data.enums import DataFeed
from dotenv import load_dotenv
import os
# Exception handling (optional)
from alpaca.common.exceptions import APIError

# Securely input your Alpaca API credentials

load_dotenv(".env")  # Explicitly load a specific .env file
API_KEY = os.environ["API_KEY"]
SECRET_KEY = os.environ["SECRET_KEY"]


# Import necessary libraries


# Initialize the historical data client
def get_data(ticker,start_date,end_date,time_frame):
    client = StockHistoricalDataClient(API_KEY, SECRET_KEY)

    num=time_frame["number"]
    unit=time_frame["unit"]

    if(unit=="min"):
        unit=TimeFrameUnit.Minute
    # Define the time range in UTC
     # Approximately 6 months

    # Create the request parameters with IEX feed (free data)
    request_params = StockBarsRequest(
        symbol_or_symbols=ticker,
        start=start_date,
        end=end_date,
        timeframe=TimeFrame(num, unit),
        feed=DataFeed.IEX,  # Use IEX data feed
        limit=10000  # Adjust as needed
    )

    # Fetch the data
    bars = client.get_stock_bars(request_params)
    return bars

# Check if data is returned
# if bars.df.empty:
#     print("No data was returned. Please check your API access and parameters.")
# else:
#     # Convert the data to a pandas DataFrame
#     tsla_data = bars.df.reset_index()

#     # Display the first few rows
#     print("First 5 rows of TSLA 30-minute interval data:")
#     display(tsla_data.head())

#     # Optionally, plot the closing prices
#     tsla_data.set_index('timestamp', inplace=True)
#     tsla_data['close'].plot(title='TSLA Close Prices over Past 6 Months (30-minute intervals)', figsize=(15,7))

#     # Reset index for saving
#     tsla_data.reset_index(inplace=True)

#     # Save to CSV in Google Colab
#     tsla_data.to_csv('tsla_30min_past6months.csv', index=False)
#     print("\nData saved to 'tsla_30min_past6months.csv' in the Colab environment.")
#     tsla_data.set_index('timestamp', inplace=True)
#     tsla_data.index = tsla_data.index.tz_localize(None)

# get_tsla_data()

if __name__ == "__main__":
    end_date = datetime.now(pytz.utc)
    start_date = end_date - timedelta(days=180 * 10) 
    time_frame={"number":30,"unit":"min"}
    bars=get_data('TSLA',start_date,end_date,time_frame)
    print(bars)

    pass

