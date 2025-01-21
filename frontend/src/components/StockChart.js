import React from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";

// Register the required chart types
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const StockChart = ({ data }) => {
  if (!data) {
    return <p>No data available. Submit the form to see results.</p>;
  }

  const chartData = {
    labels: data.results.map((entry) => `Day ${entry.day}`),
    datasets: [
      {
        label: `Portfolio Value (${data.symbol})`,
        data: data.results.map((entry) => entry.value),
        borderColor: "rgba(75,192,192,1)",
        backgroundColor: "rgba(75,192,192,0.2)",
        fill: true,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { position: "top" },
    },
    scales: {
      y: { beginAtZero: false },
    },
  };

  return <Line data={chartData} options={options} />;
};

export default StockChart;
