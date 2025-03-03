// CrewView.js - Component to display crew scheduling details

import React from 'react';

const CrewView = ({ crew }) => {
  return (
    <div className="p-4 bg-white shadow rounded">
      <h2 className="text-2xl font-semibold mb-2">Crew Scheduling Details</h2>
      {crew && crew.length > 0 ? (
        <table className="min-w-full table-auto">
          <thead>
            <tr className="bg-gray-200">
              <th className="px-4 py-2">Crew ID</th>
              <th className="px-4 py-2">Name</th>
              <th className="px-4 py-2">Role</th>
              <th className="px-4 py-2">Fatigue Score</th>
              <th className="px-4 py-2">Last Scheduled</th>
            </tr>
          </thead>
          <tbody>
            {crew.map((member) => (
              <tr key={member.crew_id} className="text-center">
                <td className="border px-4 py-2">{member.crew_id}</td>
                <td className="border px-4 py-2">{member.name}</td>
                <td className="border px-4 py-2">{member.role}</td>
                <td className="border px-4 py-2">{member.fatigue_score}</td>
                <td className="border px-4 py-2">{member.last_scheduled}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No crew data available.</p>
      )}
    </div>
  );
};

export default CrewView;
