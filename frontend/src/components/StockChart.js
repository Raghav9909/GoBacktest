import React, { useState } from "react";
import { Line } from "react-chartjs-2";

const StockChart = () => {
  const [chartData, setChartData] = useState({
    labels: [],
    datasets: [],
  });

  const updateChart = (data) => {
    setChartData({
      labels: data.results.map((entry) => `Day ${entry.day}`),
      datasets: [
        {
          label: `Portfolio Value (${data.symbol})`,
          data: data.results.map((entry) => entry.value),
          borderColor: "rgba(75,192,192,1)",
          fill: false,
        },
      ],
    });
  };

  return (
    <div>
      {chartData.labels.length > 0 ? (
        <Line data={chartData} />
      ) : (
        <p>Submit the form to see backtesting results.</p>
      )}
    </div>
  );
};

export default StockChart;
