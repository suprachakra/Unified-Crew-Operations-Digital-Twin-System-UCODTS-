import React from "react";

const PersonalFatigueMonitor = ({ crewId, alertnessScore }) => (
  <div>
    <h3>Crew {crewId} Fatigue Monitor</h3>
    <p>Current Alertness: {alertnessScore}</p>
  </div>
);

export default PersonalFatigueMonitor;
