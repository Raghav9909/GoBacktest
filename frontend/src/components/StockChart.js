import React from "react";
import { Line } from "react-chartjs-2";
import { Card, CardContent, Typography } from "@mui/material";

const StockChart = ({ data }) => {
  // Ensure data is valid and contains results
  if (!data || !data.results || !Array.isArray(data.results)) {
    return (
      <Card>
        <CardContent>
          <Typography variant="body2">No data available for backtesting.</Typography>
        </CardContent>
      </Card>
    );
  }

  // Extracting data for the chart
  const chartData = {
    labels: data.results.map((entry) => `Day ${entry.day}`),
    datasets: [
      {
        label: "Portfolio Value",
        data: data.results.map((entry) => entry.value),
        borderColor: "cyan",
        backgroundColor: "rgba(0,255,255,0.2)",
        tension: 0.3,
      },
    ],
  };

  return (
    <Card>
      <CardContent>
        <Typography variant="h5">Backtesting Results</Typography>
        <Line data={chartData} />
      </CardContent>
    </Card>
  );
};

export default StockChart;
