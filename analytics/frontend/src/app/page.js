// pages/analytics.js
"use client";
import React, { useEffect, useState } from "react";

export default function AnalyticsPage() {
  const [metrics, setMetrics] = useState([]);

  useEffect(() => {
    // Fetch from your Django endpoint
    fetch("http://127.0.0.1:8000/en/analytics/api/business-metrics/")
      .then((response) => response.json())
      .then((data) => {
        setMetrics(data);
      })
      .catch((error) => {
        console.error("Error fetching business metrics:", error);
      });
  }, []);

  return (
    <div>
      <h1>Business Metrics Dashboard</h1>
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Total Views</th>
            <th>CTR Contact Button</th>
          </tr>
        </thead>
        <tbody>
          {metrics.map((metric) => (
            <tr key={metric.id}>
              <td>{metric.date}</td>
              <td>{metric.total_views}</td>
              <td>{metric.ctr_contact_button}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
