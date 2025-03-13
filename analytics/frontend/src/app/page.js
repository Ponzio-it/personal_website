import DashboardLayout from '@/components/layout/DashboardLayout';
import BusinessMetricsDashboard from '@/components/dashboards/BusinessMetricsDashboard';

export default function HomePage() {
  return (
    <DashboardLayout>
        <BusinessMetricsDashboard />
    </DashboardLayout>
  );
}