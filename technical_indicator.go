package rsi_calculator

import (
	"fmt"
)

// CalculateRSI calculates the Relative Strength Index (RSI).
// prices: slice of float64 representing the price values.
// period: the number of periods for the RSI calculation.
func CalculateRSI(prices []float64, period int) ([]float64, error) {
	if len(prices) < period+1 {
		return nil, fmt.Errorf("not enough prices to calculate RSI")
	}

	// Resultant RSI values
	rsi := make([]float64, len(prices)-period)

	// Calculate initial averages
	var gainSum, lossSum float64
	for i := 1; i <= period; i++ {
		change := prices[i] - prices[i-1]
		if change > 0 {
			gainSum += change
		} else {
			lossSum -= change // use the negative change for loss
		}
	}

	
	avgGain := gainSum / float64(period)
	avgLoss := lossSum / float64(period)

	// Calculate the RSI for each subsequent price
	for i := period; i < len(prices); i++ {
		change := prices[i] - prices[i-1]
		var gain, loss float64
		if change > 0 {
			gain = change
		} else {
			loss = -change
		}

		// Smoothed averages
		avgGain = ((avgGain * float64(period-1)) + gain) / float64(period)
		avgLoss = ((avgLoss * float64(period-1)) + loss) / float64(period)

		// Avoid division by zero
		if avgLoss == 0 {
			rsi[i-period] = 100
		} else {
			rs := avgGain / avgLoss
			rsi[i-period] = 100 - (100 / (1 + rs))
		}
	}

	return rsi, nil
}
