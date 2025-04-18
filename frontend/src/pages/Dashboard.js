import React, { useEffect, useState } from 'react';

const Dashboard = () => {
  const [data, setData] = useState({
    flightsOnTime: 0,
    complianceAlerts: 0,
    crewUtilization: 0,
    co2Emissions: 0
  });

  useEffect(() => {
    // In production, fetch aggregated metrics from a backend endpoint or API gateway.
    setData({
      flightsOnTime: 96,
      complianceAlerts: 0,
      crewUtilization: 85,
      co2Emissions: 12345
    });
  }, []);

  return (
    <div>
      <h1>UCODTS Global Dashboard</h1>
      <ul>
        <li>On-Time Flight Rate: {data.flightsOnTime}%</li>
        <li>Compliance Alerts: {data.complianceAlerts}</li>
        <li>Crew Utilization: {data.crewUtilization}%</li>
        <li>Total CO₂ Emissions (kg): {data.co2Emissions}</li>
      </ul>
    </div>
  );
};

export default Dashboard;
