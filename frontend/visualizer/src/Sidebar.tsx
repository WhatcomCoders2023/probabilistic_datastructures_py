import React from 'react';
import Slider from 'react-input-slider';

interface SidebarProps {
  capacity: number;
  numHashFunctions: number;
  falsePositiveRate: number;
  handleCapacityChange: (value: number) => void;
  handleNumHashFunctionsChange: (value: number) => void;
  handleFalsePositiveRateChange: (value: number) => void;
  handleConfirm: () => void;
}

const SideBar: React.FC<SidebarProps> = ({
  capacity,
  numHashFunctions,
  falsePositiveRate,
  handleCapacityChange,
  handleNumHashFunctionsChange,
  handleFalsePositiveRateChange,
  handleConfirm,
}) => {
  return (
    <div
      style={{
        width: '300px',
        padding: '20px',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      <h2>Settings</h2>
      <div>
        <label>Capacity: {capacity}</label>
        <Slider
          axis="x"
          x={capacity}
          xmax={10000}
          onChange={({ x }) => handleCapacityChange(x)}
        />
      </div>
      <div>
        <label>Number of Hash Functions: {numHashFunctions}</label>
        <Slider
          axis="x"
          x={numHashFunctions}
          xmax={10}
          onChange={({ x }) => handleNumHashFunctionsChange(x)}
        />
      </div>
      <div>
        <label>False Positive Rate: {falsePositiveRate.toFixed(2)}</label>
        <Slider
          axis="x"
          x={falsePositiveRate}
          xmax={1}
          xstep={0.01}
          onChange={({ x }) => handleFalsePositiveRateChange(x)}
        />
      </div>
      <button onClick={handleConfirm}>Confirm</button>
    </div>
  );
};

export default SideBar;
