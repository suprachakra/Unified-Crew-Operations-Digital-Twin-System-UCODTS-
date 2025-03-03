import React, { useEffect, useState } from 'react';
import { getCrewList } from '../utils/api';

const Dashboard = () => {
  const [crew, setCrew] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getCrewList()
      .then((data) => {
        setCrew(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error fetching crew list:', error);
        setLoading(false);
      });
  }, []);

  return (
    <div className="container">
      <h1 className="text-3xl font-bold mb-4">UCODTS Dashboard</h1>
      {loading ? (
        <p>Loading data...</p>
      ) : (
        <div>
          <h2 className="text-xl font-semibold">Crew Status</h2>
          <ul>
            {crew.map((member) => (
              <li key={member.crew_id}>
                {member.name} ({member.role}) - Fatigue Score: {member.fatigue_score}
              </li>
            ))}
          </ul>
          {/* Additional dashboard widgets and data visualizations can be added here */}
        </div>
      )}
    </div>
  );
};

export default Dashboard;
