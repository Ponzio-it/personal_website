"use client";

import {
     FunnelChart as ReFunnelChart, 
     Funnel, 
     Tooltip, 
     ResponsiveContainer, 
     LabelList 
    } from 'recharts';

const FunnelChart = ({ data, dataKey, nameKey}) => {
  return (
    <div className="chart-container">
      <ResponsiveContainer width="100%" height={300}>
        <ReFunnelChart>
          <Funnel data={data} dataKey={dataKey} nameKey={nameKey} fill="#8884d8">
            <LabelList position="right" fill="#000" stroke="none" />
          </Funnel>
          <Tooltip />
        </ReFunnelChart>
      </ResponsiveContainer>
    </div>
  );
};

export default FunnelChart;
