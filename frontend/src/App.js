import React, { useState } from "react";
import { Container, Typography, Grid, Card, CardContent } from "@mui/material";
import StockForm from "./components/StockForm";
import StockChart from "./components/StockChart";

function App() {
  const [backtestData, setBacktestData] = useState({});
  
  // const [alpacaData, setAlpacaData] = useState(null);

  const handleBacktestSubmit = (data) => {
    console.log("reached here")
    const newItem = { data };
    // const newItem = {
    //   "ticker": "TSLA",
    //   "start_date": "2025-01-08",
    //   "end_date": "2025-01-20",
    //   "strategy": "SMA",
    //   "timeframe": {
    //     "num": 30,
    //     "unit": "min"
    //   }
    // }
  console.log(JSON.stringify(newItem.data))

    // Send data to the backend
    fetch('http://localhost:5000/posting_stock_info', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newItem.data),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log('Item created:', data);
        setBacktestData(data); 

        // Optionally reset form or navigate
        // setName('');
      })
      .catch((err) => {
        console.error('Error creating item:', err);
      });
    // Update the backtest data when the form is submitted
  };

  return (
    <Container maxWidth="lg" style={{ marginTop: "20px" }}>
      <Typography variant="h3" align="center" gutterBottom>
        Stock Backtesting Showcase
      </Typography>
      <Grid container spacing={3}>
        {/* Input Form */}
        <Grid item xs={12} sm={6}>
          <Card>
            <CardContent>
              <Typography variant="h5" gutterBottom>
                Configure Backtesting
              </Typography>
              <StockForm onSubmit={handleBacktestSubmit} />
            </CardContent>
          </Card>
        </Grid>

        {/* Visualization */}
        <Grid item xs={12} sm={6}>
          <Card>
            <CardContent>
              <Typography variant="h5" gutterBottom>
                Backtesting Results
              </Typography>
              {backtestData ? (
                <StockChart data={backtestData} />
              ) : (
                <Typography variant="body2">No data available yet.</Typography>
              )}
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Container>
  );
}

export default App;
