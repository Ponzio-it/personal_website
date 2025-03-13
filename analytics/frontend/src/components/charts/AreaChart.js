"use client";

import {
  AreaChart as ReAreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts';

/**
 * @param {Array} data - The array of data objects for the chart
 * @param {string} xKey - The property name for x-axis (e.g., 'month')
 * @param {string} yKey1 - The property name for the first area series
 * @param {string} yKey2 - The property name for the second area series
 * @param {string} title - Title displayed above the chart
 */
const AreaChart = ({ data, xKey, yKey1, yKey2}) => {
  return (
    <div className="chart-container">
      <ResponsiveContainer width="100%" height={300}>
        <ReAreaChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey={xKey} />
          <YAxis />
          <Tooltip />
          <Legend />

          {/*
            First overlapping area
            Fill opacity is reduced to see overlapping sections clearly
          */}
          <Area
            type="monotone"
            dataKey={yKey1}
            stroke="#8884d8"
            fill="#8884d8"
            fillOpacity={0.3}
          />

          {/*
            Second overlapping area
            A different color so users can distinguish areas
          */}
          <Area
            type="monotone"
            dataKey={yKey2}
            stroke="#82ca9d"
            fill="#82ca9d"
            fillOpacity={0.3}
          />
        </ReAreaChart>
      </ResponsiveContainer>
    </div>
  );
};

export default AreaChart;
