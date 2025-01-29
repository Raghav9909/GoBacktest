import React, { useState } from "react";
import { TextField, Button, MenuItem } from "@mui/material";

const StockForm = ({ onSubmit }) => {
  const [ticker, setTicker] = useState("");
  const [strategy, setStrategy] = useState("SMA");
  const [start_date, setStartDate] = useState("");
  const [end_date, setEndDate] = useState("");
  // Store timeframe as an object with "num" and "unit" properties
  const [timeframe, setTimeframe] = useState({ num: 0, unit: "" });

  const handleSubmit = () => {
    // Generate dummy backtesting data
    const dummyData = {
      ticker,
      start_date,
      end_date,
      strategy,
      timeframe // pass the entire timeframe object
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
        value={ticker}
        onChange={(e) => setTicker(e.target.value)}
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
        value={start_date}
        onChange={(e) => setStartDate(e.target.value)}
      />

      <TextField
        label="End Date"
        type="date"
        InputLabelProps={{ shrink: true }}
        fullWidth
        margin="normal"
        value={end_date}
        onChange={(e) => setEndDate(e.target.value)}
      />

      {/* Timeframe Fields */}
      <TextField
        label="Time frame number"
        variant="outlined"
        fullWidth
        type="number"
        margin="normal"
        value={timeframe.num}
        onChange={(e) =>
          setTimeframe((prev) => ({ ...prev, num: e.target.value }))
        }
      />
      <p>Try typing 30, 60, etc.</p>

      <TextField
        label="Time frame unit"
        variant="outlined"
        fullWidth
        margin="normal"
        value={timeframe.unit}
        onChange={(e) =>
          setTimeframe((prev) => ({ ...prev, unit: e.target.value }))
        }
      />
      <p>Try typing min, day, or hour</p>

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
