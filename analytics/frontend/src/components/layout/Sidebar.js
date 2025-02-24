// src/components/layout/Sidebar.js
"use client"; // Client component since it handles user interactions

import React, { useState } from "react";
import styles from "./Sidebar.module.css";

const dashboards = [
  { id: "business", name: "Business Metrics" },
  { id: "engagement", name: "Engagement Metrics" },
  { id: "security", name: "Security Metrics" },
];

const Sidebar = ({ onSelectDashboard }) => {
  const [activeDashboard, setActiveDashboard] = useState(dashboards[0].id);

  const handleDashboardChange = (id) => {
    setActiveDashboard(id);
    onSelectDashboard(id); // Notify parent component
  };

  return (
    <div className={styles.sidebar}>
      <h2 className={styles.title}>Dashboards</h2>
      <ul className={styles.menu}>
        {dashboards.map((dashboard) => (
          <li
            key={dashboard.id}
            className={`${styles.menuItem} ${activeDashboard === dashboard.id ? styles.active : ""}`}
            onClick={() => handleDashboardChange(dashboard.id)}
          >
            {dashboard.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Sidebar;
