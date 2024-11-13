import React, { useState } from 'react';
import CraftingForm from './components/CraftingForm';
import TreeVisualization from './components/TreeVisualization';

function App() {
  const [nodes, setNodes] = useState([]);
  const [edges, setEdges] = useState([]);

  const handleCalculate = (itemName, quantity) => {
    fetch('http://localhost:5000/calculate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ item_name: itemName, quantity: quantity }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.nodes && data.edges) {
          setNodes(data.nodes);
          setEdges(data.edges);
        } else {
          console.error('Error:', data.error);
        }
      })
      .catch((error) => console.error('Error:', error));
  };

  return (
    <div className="App">
      <h1>Factory Resource Planner</h1>
      <CraftingForm onCalculate={handleCalculate} />
      <TreeVisualization nodes={nodes} edges={edges} />
    </div>
  );
}

export default App;
