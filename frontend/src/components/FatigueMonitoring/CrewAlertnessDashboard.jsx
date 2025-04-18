import React, { useEffect, useState } from "react";

const CrewAlertnessDashboard = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Replace with API call in production.
    setData([
      { crewId: 1, alertness: 0.85 },
      { crewId: 2, alertness: 0.60 },
      { crewId: 3, alertness: 0.45 },
    ]);
  }, []);

  return (
    <div>
      <h2>Crew Alertness Dashboard</h2>
      <table>
        <thead>
          <tr>
            <th>Crew ID</th>
            <th>Alertness Score</th>
          </tr>
        </thead>
        <tbody>
          {data.map((d) => (
            <tr key={d.crewId}>
              <td>{d.crewId}</td>
              <td>{d.alertness}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CrewAlertnessDashboard;
