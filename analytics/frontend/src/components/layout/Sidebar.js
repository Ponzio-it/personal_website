// ./components/Sidebar.jsx
"use client"
import { useState, useEffect } from 'react';
import { usePathname } from "next/navigation";
import Link from 'next/link';
import '@/styles/Sidebar.css';

export default function Sidebar() {
  const [isOpen, setIsOpen] = useState(false);
  const pathname = usePathname();

  const handleSidebarToggle = () => {
    setIsOpen((prevIsOpen) => !prevIsOpen);
  };

  // Automatically close the sidebar when the route changes
  useEffect(() => {
    setIsOpen(false);
  }, [pathname]);


  return (
    <>
    <nav className={`sidebar ${isOpen ? 'open' : ''}`} aria-label="Dashboard navigation">
      {/* Hamburger Menu Button */}
      <button
        type="button"
        className="menu-toggle"
        onClick={handleSidebarToggle}
        aria-label={isOpen ? 'Close navigation menu' : 'Open navigation menu'}
        aria-expanded={isOpen}
        aria-controls="sidebarMenu"
      >
        {/* You can replace the text or icon below with any hamburger or close icon */}
        {isOpen ? '✕' : '☰'}
      </button>

      {/* Actual sidebar links */}
      <ul id="sidebarMenu">
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
     {/* Background Overlay */}
     {isOpen && (
      <div
        className="sidebar-overlay"
        onClick={handleSidebarToggle}
        aria-hidden="true"
      />
    )}
    </>

  );
}
