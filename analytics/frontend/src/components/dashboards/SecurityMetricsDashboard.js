// SecurityMetrics.jsx
import Card from '@/components/ui/Card';

const SecurityMetrics = () => {
  return (
    <div className="dashboard-section">
      <h1>Security Metrics</h1>
      <div className="cards-grid">
        <Card title="Login Attempts">Chart here</Card>
        <Card title="Security Incidents">Chart here</Card>
        <Card title="Password Resets">Chart here</Card>
      </div>
    </div>
  );
};

export default SecurityMetrics;
