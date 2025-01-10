package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"strconv"
	"time"
)

// Candle represents a single stock price data point.
type Candle struct {
	Date   time.Time
	Open   float64
	High   float64
	Low    float64
	Close  float64
	Volume int
}

// Signal represents buy/sell signals from an external algorithm.
type Signal struct {
	Date   time.Time
	Action string // "BUY" or "SELL"
}

// LoadCandleData reads historical stock data from a CSV file.
func LoadCandleData(filename string) ([]Candle, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	reader := csv.NewReader(file)
	lines, err := reader.ReadAll()
	if err != nil {
		return nil, err
	}

	var candles []Candle
	for _, line := range lines[1:] { // Skip header
		date, _ := time.Parse("2006-01-02", line[0])
		open, _ := strconv.ParseFloat(line[1], 64)
		high, _ := strconv.ParseFloat(line[2], 64)
		low, _ := strconv.ParseFloat(line[3], 64)
		close, _ := strconv.ParseFloat(line[4], 64)
		volume, _ := strconv.Atoi(line[5])

		candles = append(candles, Candle{
			Date:   date,
			Open:   open,
			High:   high,
			Low:    low,
			Close:  close,
			Volume: volume,
		})
	}
	return candles, nil
}

// LoadSignals reads buy/sell signals from a CSV file.
func LoadSignals(filename string) ([]Signal, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	reader := csv.NewReader(file)
	lines, err := reader.ReadAll()
	if err != nil {
		return nil, err
	}

	var signals []Signal
	for _, line := range lines[1:] { // Skip header
		date, _ := time.Parse("2006-01-02", line[0])
		action := line[1]

		signals = append(signals, Signal{
			Date:   date,
			Action: action,
		})
	}
	return signals, nil
}

// Backtest executes the strategy using candles and external signals.
func Backtest(candles []Candle, signals []Signal) float64 {
	capital := 10000.0 // Initial capital
	shares := 0

	// Map signals by date for quick lookup
	signalMap := make(map[time.Time]string)
	for _, signal := range signals {
		signalMap[signal.Date] = signal.Action
	}

	for _, candle := range candles {
		if action, found := signalMap[candle.Date]; found {
			if action == "BUY" && shares == 0 {
				shares = int(capital / candle.Close)
				capital -= float64(shares) * candle.Close
				fmt.Printf("BUY on %s at $%.2f, Shares: %d\n", candle.Date.Format("2006-01-02"), candle.Close, shares)
			} else if action == "SELL" && shares > 0 {
				capital += float64(shares) * candle.Close
				fmt.Printf("SELL on %s at $%.2f, Capital: $%.2f\n", candle.Date.Format("2006-01-02"), candle.Close, capital)
				shares = 0
			}
		}
	}

	// Final portfolio value
	if shares > 0 {
		capital += float64(shares) * candles[len(candles)-1].Close
	}
	return capital
}

func main() {
	// Load historical stock data (Tesla)
	candles, err := LoadCandleData("tesla_data.csv")
	if err != nil {
		log.Fatalf("Error loading candle data: %v", err)
	}

	// Load external algorithm signals
	signals, err := LoadSignals("algorithm_signals.csv")
	if err != nil {
		log.Fatalf("Error loading signals: %v", err)
	}

	// Run backtest
	finalCapital := Backtest(candles, signals)
	fmt.Printf("Final Portfolio Value: $%.2f\n", finalCapital)
}
