import React, { useState } from "react";

const ScheduleSwap = () => {
  const [swapInfo, setSwapInfo] = useState({});

  const handleSwap = () => {
    // Dummy swap action.
    setSwapInfo({ message: "Swap initiated between Crew A and Crew B." });
  };

  return (
    <div>
      <h1>Crew Schedule Swap</h1>
      <button onClick={handleSwap}>Initiate Swap</button>
      {swapInfo.message && <p>{swapInfo.message}</p>}
    </div>
  );
};

export default ScheduleSwap;
