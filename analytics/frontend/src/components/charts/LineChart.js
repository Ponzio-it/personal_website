"use client"
import {
    LineChart as ReLineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    Legend,
    ResponsiveContainer,
  } from 'recharts';
  
  const LineChart = ({ data, xKey, yKey }) => {
    return (
      <ResponsiveContainer width="100%" height={300}>
        <ReLineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey={xKey} label={{ value: 'Months', position: 'insideBottom', offset: -5 }} />
          <YAxis label={{ value: 'Total Views', angle: -90, position: 'insideLeft' }} />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey={yKey} stroke="#8884d8" strokeWidth={2} activeDot={{ r: 8 }} />
        </ReLineChart>
      </ResponsiveContainer>
    );
  };
  
  export default LineChart;
  