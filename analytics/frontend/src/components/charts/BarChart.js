"use client"
import {
    BarChart as ReBarChart,
    Bar,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    Legend,
    ResponsiveContainer,
  } from 'recharts';
  
const BarChart = ({ data, xKey, yKey, title }) => {
    return (
      <div style={{ width: '100%', height: 300 }}>
        <h2>{title}</h2>
        <ResponsiveContainer width="100%" height="100%">
          <ReBarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey={xKey} label={{ value: 'Months', position: 'insideBottom', offset: -5 }} />
            <YAxis label={{ value: 'Total Views', angle: -90, position: 'insideLeft' }} />
            <Tooltip />
            <Legend />
            <Bar dataKey={yKey} fill="#6366f1" />
          </ReBarChart>
        </ResponsiveContainer>
      </div>
    );
  };
  
export default BarChart;
  