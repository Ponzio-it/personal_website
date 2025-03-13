"use client";

import { 
    PieChart as RePieChart, 
    Pie, 
    Tooltip, 
    Legend, 
    ResponsiveContainer, 
    Cell 
} from 'recharts';

const COLORS = ['#8884d8', '#82ca9d', '#FFBB28', '#FF8042', '#0088FE',' #85df20'];

const PieChart = ({ data, dataKey, nameKey}) => {
  return (
    <div className="chart-container">
      <ResponsiveContainer width="100%" height={300}>
        <RePieChart>
          <Pie 
            data={data} 
            dataKey={dataKey} 
            nameKey={nameKey} 
            cx="50%" 
            cy="50%" 
            outerRadius={100} 
            fill="#8884d8"
            label
          >
            {data.map((_, index) => (
              <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
            ))}
          </Pie>
          <Tooltip />
          <Legend />
        </RePieChart>
      </ResponsiveContainer>
    </div>
  );
};

export default PieChart;
