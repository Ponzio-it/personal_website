"use client";

import Card from '@/components/ui/Card';
import BarChart from '@/components/charts/BarChart';


const visitorData = [
  { month: 'Jan', visitors: 400 },
  { month: 'Feb', visitors: 300 },
  { month: 'Mar', visitors: 500 },
];

const BusinessMetrics = () => {
  return (
    <div className="dashboard-section">
      <h1>Business Metrics</h1>
      <div className="cards-grid">

        <Card title="Total Visitors">
          <div className="chart-wrapper">
            <BarChart 
              data={visitorData} 
              xKey="month"
              yKey="visitors"
              title="Monthly Visitors"
            />
          </div>
        </Card>

        <Card title="Sales">
          <div className="chart-placeholder">Chart here</div>
        </Card>

        <Card title="Expenses">
          <div className="chart-placeholder">Chart here</div>
        </Card>

      </div>
    </div>
  );
};

export default BusinessMetrics;
