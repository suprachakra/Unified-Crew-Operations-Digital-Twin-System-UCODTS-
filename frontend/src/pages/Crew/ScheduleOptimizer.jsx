import React, { useState } from "react";

const ScheduleOptimizer = () => {
  const [optimized, setOptimized] = useState(null);

  const handleOptimize = async () => {
    try {
      const response = await fetch("/api/v1/crew/optimize");
      const data = await response.json();
      setOptimized(data.optimized_schedule || {});
    } catch (error) {
      console.error("Error optimizing schedule:", error);
    }
  };

  return (
    <div>
      <h1>Schedule Optimizer</h1>
      <button onClick={handleOptimize}>Optimize Schedule</button>
      {optimized && <pre>{JSON.stringify(optimized, null, 2)}</pre>}
    </div>
  );
};

export default ScheduleOptimizer;
