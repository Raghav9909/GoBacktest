import React, { useState } from "react";
import { Container, Typography, Grid, Card, CardContent } from "@mui/material";
import StockForm from "./components/StockForm";
import StockChart from "./components/StockChart";

function App() {
  const [backtestData, setBacktestData] = useState(null);

  const handleBacktestSubmit = (data) => {
    setBacktestData(data); // Update the backtest data when the form is submitted
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
              <StockChart data={backtestData} />
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Container>
  );
}

export default App;
