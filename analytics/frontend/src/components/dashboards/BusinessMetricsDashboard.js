"use client";

import Card from '@/components/ui/Card';
import BarChart from '@/components/charts/BarChart';
import LineChart from '@/components/charts/LineChart';
import ComboChart from '@/components/charts/ComboChart';
import FunnelChart from '@/components/charts/FunnelChart';

// Sample data for Line Chart (Monthly Revenue Trends)
const lineData = [
  { month: 'Jan', visitors: 400  },
  { month: 'Feb', visitors: 300 },
  { month: 'Mar', visitors: 500 },
  { month: 'Apr', visitors: 600 },
];

// Sample data for Combo Chart (Sales + Revenue)
const comboData = [
  { month: 'Jan', visitorsbar: 400, visitorsline: 400 },
  { month: 'Feb', visitorsbar: 300, visitorsline: 300 },
  { month: 'Mar', visitorsbar: 500, visitorsline: 500 },
  { month: 'Apr', visitorsbar: 600, visitorsline: 600 }
];

// Existing visitor data for Bar Chart
const visitorData = [
  { month: 'Jan', visitors: 400 },
  { month: 'Feb', visitors: 300 },
  { month: 'Mar', visitors: 500 },
  { month: 'Apr', visitors: 600 }
];

// Simple data for Funnel Chart
const funnelData=[
  { stage: 'Visitors', value: 600 },
  { stage: 'Signups', value: 200 },
  { stage: 'Contact', value: 50 },
]


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
              title="Monthly Visitors (bar)"
            />
          </div>
        </Card>

        <Card title="Total Visitors (line)">
        <div className="chart-wrapper">
            <LineChart 
              data={lineData} 
              xKey="month"
              yKey="visitors"
              title="Monthly Visitors (line)"
            />
        </div>
        </Card>

        <Card title="Total Visitors (combo)">
        <div className="chart-wrapper">
            <ComboChart 
              data={comboData} 
              xKey="month"
              barDataKey="visitorsbar"
              lineDataKey="visitorsline"
              title="Monthly Visitors (combo)"
            />
        </div>
        </Card>

        <Card title="Conversion Funnel">
        <div className="chart-wrapper">
            <FunnelChart 
              data={funnelData} 
              dataKey="value"
              nameKey="stage"
              title="Conversion Funnel"
              />
        </div>
        </Card>


      </div>
    </div>
  );
};

export default BusinessMetrics;
