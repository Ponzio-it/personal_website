import Sidebar from '@/components/layout/Sidebar';
import '@/styles/DashboardLayout.css';

const DashboardLayout = ({ children }) => {
  return (
    <div className="dashboard-layout">
      <Sidebar />
      <main className="dashboard-main-content">
        {children}
      </main>
    </div>
  );
};

export default DashboardLayout;
