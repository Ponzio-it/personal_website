import Link from 'next/link';
import '@/styles/Sidebar.css';

const Sidebar = () => {
  return (
    <nav className="sidebar" aria-label="Dashboard navigation">
      <ul>
        <li>
          <Link href="/analytics/business" className="sidebar-link">
            Business Metrics
          </Link>
        </li>
        <li>
          <Link href="/analytics/engagement" className="sidebar-link">
            Engagement Metrics
          </Link>
        </li>
        <li>
          <Link href="/analytics/security" className="sidebar-link">
            Security Metrics
          </Link>
        </li>
      </ul>
    </nav>
  );
};

export default Sidebar;
