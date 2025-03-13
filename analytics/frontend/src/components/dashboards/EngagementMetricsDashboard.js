import Card from '@/components/ui/Card';
import BarChart from '@/components/charts/BarChart';
import LineChart from '@/components/charts/LineChart';
import PieChart from '@/components/charts/PieChart';
import RadarChart from '@/components/charts/RadarChart';

// Sample data for Pie Chart
const pageVisitedData=[
  { category: 'Home', value: 600 },
  { category: 'Experiences', value: 300 },
  { category: 'Projects', value: 200 },
  { category: 'Contact Me', value: 400 },
  { category: 'Blog', value: 200 },
  { category: 'Analytics', value: 500 },
]

// Sample data for Bar Chart
const userSessionData = [
  { month: 'Jan', visitors: 400 },
  { month: 'Feb', visitors: 300 },
  { month: 'Mar', visitors: 500 },
  { month: 'Apr', visitors: 600 }
];

// Sample data for radar Chart
const topPageData = [
  { category: 'Home', value: 600 },
  { category: 'Experiences', value: 300 },
  { category: 'Projects', value: 200 },
  { category: 'Contact Me', value: 400 },
  { category: 'Blog', value: 200 },
  { category: 'Analytics', value: 500 },
];

// Sample data for Line Chart (Monthly Revenue Trends)
const bounceRateData = [
    { month: 'Jan', bounce_rate: 400 },
    { month: 'Feb', bounce_rate: 50 },
    { month: 'Mar', bounce_rate: 100 },
    { month: 'Apr', bounce_rate: 200 },
]

const EngagementMetrics = () => {
  return (
    <div className="dashboard-section">
      <h1>Engagement Metrics</h1>
      <div className="cards-grid">
        <Card title="Users session per month">
        <div className="chart-wrapper">
            <BarChart 
              data={userSessionData} 
              xKey="month"
              yKey="visitors"
              title="User session per months"
            />
          </div>
        </Card>

        <Card title="Top page visited">
        <div className="chart-wrapper">
              <RadarChart 
                data={topPageData}
                dataKey="value"
                categoryKey="category"
                title="Top page visited"
              />
           </div>
        </Card>
        
        <Card title="Distribution of pages visited">
        <div className="chart-wrapper">
            <PieChart 
              data={pageVisitedData} 
              dataKey="value"
              nameKey="category"
              title="Distribution of pages visited"
              />
        </div>
        </Card>

        <Card title="Bounce Rate per month">
        <div className="chart-wrapper">
            <LineChart 
              data={bounceRateData} 
              xKey="month"
              yKey="bounce_rate"
              title="Bonce Rate per month"
            />
        </div>
        </Card>
      </div>
    </div>
  );
};

export default EngagementMetrics;
