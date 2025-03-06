"use client"

import {
    ComposedChart,
    Bar,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    Legend,
    ResponsiveContainer,
  } from 'recharts';
  
  const ComboChart = ({ data, xKey, barDataKey, lineDataKey }) => {
    return (
      <ResponsiveContainer width="100%" height={350}>
        <ComposedChart data={data}>
          <CartesianGrid stroke="#f5f5f5" />
          <XAxis dataKey={xKey} label={{ value: 'Months', position: 'insideBottom', offset: -5 }} />
          <YAxis label={{ value: 'Total Views', angle: -90, position: 'insideLeft' }} />
          <Tooltip />
          <Legend />
          <Bar dataKey={barDataKey} barSize={30} fill="#8884d8" />
          <Line type="monotone" dataKey={lineDataKey} stroke="#ff7300" />
        </ComposedChart>
    </ResponsiveContainer>
    );
  };
  
  export default ComboChart;
  