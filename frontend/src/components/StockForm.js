import React, { useState } from "react";
import { TextField, Button, MenuItem } from "@mui/material";

const StockForm = ({ onSubmit }) => {
  const [symbol, setSymbol] = useState("");
  const [strategy, setStrategy] = useState("SMA");
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  const handleSubmit = () => {
    // Generate dummy backtesting data
    const dummyData = {
      symbol,
      strategy,
      results: [
        { day: 1, value: 10000 },
        { day: 2, value: 10200 },
        { day: 3, value: 10150 },
        { day: 4, value: 10400 },
        { day: 5, value: 10500 },
      ],
    };

    onSubmit(dummyData); // Pass data back to the parent (App.js)
  };

  return (
    <form>
      <TextField
        label="Stock Symbol"
        variant="outlined"
        fullWidth
        margin="normal"
        value={symbol}
        onChange={(e) => setSymbol(e.target.value)}
      />
      <p>Try typing TSLA or AAPL</p>

      <TextField
        select
        label="Strategy"
        variant="outlined"
        fullWidth
        margin="normal"
        value={strategy}
        onChange={(e) => setStrategy(e.target.value)}
      >
        <MenuItem value="SMA">Simple Moving Average</MenuItem>
        <MenuItem value="EMA">Exponential Moving Average</MenuItem>
        <MenuItem value="RSI">Relative Strength Index</MenuItem>
      </TextField>
      <TextField
        label="Start Date"
        type="date"
        InputLabelProps={{ shrink: true }}
        fullWidth
        margin="normal"
        value={startDate}
        onChange={(e) => setStartDate(e.target.value)}
      />
      <TextField
        label="End Date"
        type="date"
        InputLabelProps={{ shrink: true }}
        fullWidth
        margin="normal"
        value={endDate}
        onChange={(e) => setEndDate(e.target.value)}
      />
      <Button
        variant="contained"
        color="primary"
        onClick={handleSubmit}
        fullWidth
        style={{ marginTop: "10px" }}
      >
        Run Backtest
      </Button>
    </form>
  );
};

export default StockForm;
