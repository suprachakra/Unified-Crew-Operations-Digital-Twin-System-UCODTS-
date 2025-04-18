import React, { useState } from "react";

const CrewReassignment = () => {
  const [suggestion, setSuggestion] = useState(null);

  const handleSuggest = () => {
    // Simulate an API call that returns a crew replacement suggestion.
    const simulatedResponse = { flight_id: 123, new_crew_id: 45 };
    setSuggestion(simulatedResponse);
  };

  return (
    <div>
      <h2>Crew Reassignment</h2>
      <button onClick={handleSuggest}>Suggest Replacement</button>
      {suggestion && (
        <div>
          <p>
            Flight {suggestion.flight_id} will be reassigned to Crew{" "}
            {suggestion.new_crew_id}.
          </p>
        </div>
      )}
    </div>
  );
};

export default CrewReassignment;
