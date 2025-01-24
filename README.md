# How to run locally 
For terminal python run uvicorn app:app --reload
for run go backtest.go

for react run npm star after npm install
# GoTradeSim

GoTradeSim is a Go-based stock backtesting framework that allows you to test and evaluate trading strategies using historical and real-time market data. The framework integrates external trading signals, supports modular components, and provides features like data simulation and real-time data handling for robust strategy evaluation.

---

## Features

- **Historical Data Processing**: Load historical stock data from CSV files.
- **Signal Integration**: Supports external buy/sell signals for algorithmic trading.
- **Backtesting**: Simulates trading strategies on historical or real-time data.
- **Real-Time Data Handling**: Fetch real-time market data from APIs (e.g., Alpha Vantage, Yahoo Finance).
- **Customizable**: Configurable strategy inputs and modular architecture.
- **Simulated Real-Time Mode**: Test strategies with historical data as if it were live.

---

## Prerequisites

- **Go**: Install [Go](https://golang.org/doc/install).
- **API Key** (for real-time data): Obtain an API key from a stock data provider (e.g., Alpha Vantage, Polygon.io).

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/GoTradeSim.git
   cd GoTradeSim
   ```

2. Install dependencies (if any):
   ```bash
   go mod tidy
   ```

3. Build the project:
   ```bash
   go build
   ```

---

## Usage

### 1. Load Historical Data
Prepare a CSV file (`tesla_data.csv`) with the following format:

```csv
Date,Open,High,Low,Close,Volume
2024-01-01,400,410,390,405,1000000
2024-01-02,405,415,395,410,1100000
...
```

### 2. Load External Signals
Prepare a CSV file (`algorithm_signals.csv`) with the following format:

```csv
Date,Action
2024-01-03,BUY
2024-01-08,SELL
...
```

### 3. Run the Backtest

#### Historical Backtest:
Run a backtest using historical data:

```bash
go run main.go
```

#### Simulated Real-Time Backtest:
Use historical data to simulate real-time behavior:

```bash
go run main.go --simulate
```

#### Real-Time Data Backtest:
Fetch real-time data for backtesting (requires API key):

```bash
go run main.go --realtime --symbol=TSLA --apikey=YOUR_API_KEY
```

---

## Example Output

```plaintext
BUY on 2024-01-03 at $415.00, Shares: 24
SELL on 2024-01-08 at $440.00, Capital: $10,600.00
Final Portfolio Value: $10,485.00
```

---

## Configuration

Modify the following parameters in the code:

- **Initial Capital**: Default is `$10,000`.
- **Real-Time API Endpoint**: Update the API URL and authentication details for your data provider.
- **Simulation Delay**: Adjust `time.Sleep` interval for simulated real-time behavior.

---

## Future Enhancements

- Add support for more technical indicators (e.g., RSI, Bollinger Bands).
- Implement advanced risk management features (e.g., stop-loss, take-profit).
- Include multi-stock portfolio backtesting.
- Visualize performance with charts.

---