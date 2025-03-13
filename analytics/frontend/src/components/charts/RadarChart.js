"use client";

import { RadarChart as ReRadarChart, 
    PolarGrid, 
    PolarAngleAxis, 
    Radar, 
    Tooltip, 
    Legend, 
    ResponsiveContainer 
} from 'recharts';

const RadarChart = ({ data, dataKey, categoryKey}) => {
  return (
    <div className="chart-container">
      <ResponsiveContainer width="100%" height={300}>
        <ReRadarChart outerRadius="80%" data={data}>
          <PolarGrid />
          <PolarAngleAxis dataKey={categoryKey} />
          <Radar dataKey={dataKey} stroke="#8884d8" fill="#8884d8" fillOpacity={0.6} />
          <Tooltip />
          <Legend />
        </ReRadarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default RadarChart;
