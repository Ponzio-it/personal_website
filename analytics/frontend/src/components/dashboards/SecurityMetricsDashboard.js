// SecurityMetrics.jsx
import Card from '@/components/ui/Card';
import BarChart from '@/components/charts/BarChart';
import LineChart from '@/components/charts/LineChart';
import PieChart from '@/components/charts/PieChart';
import AreaChart from '@/components/charts/AreaChart';

// Sample data for Pie Chart
const loginAttemptData=[
  { category: 'Succesful Login', value: 600 },
  { category: 'Failure Login', value: 300 },
]

// Sample data for Line Chart (Monthly Revenue Trends)
const activeSessionData = [
  { month: 'Jan', active_session: 400  },
  { month: 'Feb', active_session: 300 },
  { month: 'Mar', active_session: 500 },
  { month: 'Apr', active_session: 600 },
];

// Existing visitor data for Bar Chart
const errorLogData = [
  { month: 'Jan', error_log: 200 },
  { month: 'Feb', error_log: 100 },
  { month: 'Mar', error_log: 300 },
  { month: 'Apr', error_log: 150 }
];

//Sample active session error log data for Area Chart
const activeErrorData=[
    { month: 'Jan', activeSession: 400, error: 200 },
    { month: 'Feb', activeSession: 300, error: 100 },
    { month: 'Mar', activeSession: 500, error: 300 },
    { month: 'Apr', activeSession: 600, error: 150 },
  ];
  

const SecurityMetrics = () => {
  return (
    <div className="dashboard-section">
      <h1>Security Metrics</h1>
      <div className="cards-grid">
        <Card title="Login Attempts">
        <div className="chart-wrapper">
            <PieChart 
              data={loginAttemptData} 
              dataKey="value"
              nameKey="category"
              title="login Attempts"
              />
        </div>
        </Card>

        <Card title="Active session per month">
        <div className="chart-wrapper">
            <LineChart 
              data={activeSessionData} 
              xKey="month"
              yKey="active_session"
              title="Active session per month"
            />
        </div>
        </Card>

        
        <Card title="Error log per month">
        <div className="chart-wrapper">
            <BarChart 
              data={errorLogData} 
              xKey="month"
              yKey="error_log"
              title="Error log per month"
            />
          </div>
        </Card>

        <Card title="Monthly active session vs Monthly Error log">
        <div className="chart-wrapper">
              <AreaChart
              data={activeErrorData}
              xKey="month"
              yKey1="activeSession"
              yKey2="error"
              title="Monthly active session vs Monthly Error log"
            />
        </div>
        </Card>
      </div>
    </div>
  );
};

export default SecurityMetrics;
