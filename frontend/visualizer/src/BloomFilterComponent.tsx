import React, { useEffect, useState } from 'react';
import axios from 'axios';
import SideBar from './Sidebar';

interface BloomFilterData {
  exists: boolean;
}

interface Item {
  value: string;
}

const BloomFilterComponent: React.FC = () => {
  const [filterData, setFilterData] = useState<BloomFilterData | null>(null);
  const [inputItem, setInputItem] = useState<string>('');
  const [items, setItems] = useState<Item[]>([]);
  const [capacity, setCapacity] = useState<number>(5000);
  const [numHashFunctions, setNumHashFunctions] = useState<number>(5);
  const [falsePositiveRate, setFalsePositiveRate] = useState<number>(0.05);

  const checkItem = () => {
    axios
      .get<BloomFilterData>(
        `http://127.0.0.1:5000/api/bloom-filter?item=${inputItem}`
      )
      .then((response) => {
        console.log(response.data);
        setFilterData(response.data);
      })
      .catch((err) => console.error(err));
  };

  const addItem = () => {
    axios
      .post('http://127.0.0.1:5000/api/bloom-filter', { item: inputItem })
      .then((response) => {
        console.log(response.data.message);
        setItems([...items, { value: inputItem }]);
        setInputItem('');
      })
      .catch((err) => console.error(err));
  };

  const handleConfirm = () => {
    // handle the confirmation of the new parameters
    // here you could call an API to update the parameters on the server side
    // for this example, we just console.log the new parameters
    axios
      .post('http://127.0.0.1:5000/api/bloom-filter/settings', {
        capacity,
        falsePositiveRate: falsePositiveRate,
        numHashFunctions: numHashFunctions,
      })
      .then((response) => {
        console.log(response.data.message);
      })
      .catch((err) => console.error(err));
  };

  const renderHashArrays = () => {
    let hashArrays = [];
    for (let i = 0; i < numHashFunctions; i++) {
      let height = Math.log(capacity) * 60;
      console.log(height);
      hashArrays.push(
        <div
          key={i}
          style={{
            display: 'flex',
            flexWrap: 'wrap',
            width: `100px`,
            height: `${height}px`,
            border: '1px solid black',
            marginRight: '20px',
          }}
        ></div>
      );
    }
    return hashArrays;
  };

  return (
    <div style={{ display: 'flex' }}>
      <div style={{ flex: 1 }}>
        <input
          type="text"
          value={inputItem}
          onChange={(e) => setInputItem(e.target.value)}
        />
        <button onClick={addItem}>Add Item</button>
        <button onClick={checkItem}>Check Item</button>
        {filterData && (
          <div>Item exists: {filterData.exists ? 'Yes' : 'No'}</div>
        )}

        <div style={{ display: 'flex', overflowX: 'scroll' }}>
          {renderHashArrays()}
        </div>

        <SideBar
          capacity={capacity}
          numHashFunctions={numHashFunctions}
          falsePositiveRate={falsePositiveRate}
          handleCapacityChange={setCapacity}
          handleNumHashFunctionsChange={setNumHashFunctions}
          handleFalsePositiveRateChange={setFalsePositiveRate}
          handleConfirm={handleConfirm}
        />
      </div>
    </div>
  );
};

export default BloomFilterComponent;
