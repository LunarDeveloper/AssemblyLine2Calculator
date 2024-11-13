import React, { useState } from 'react';

const CraftingForm = ({ onCalculate }) => {
  const [itemName, setItemName] = useState('');
  const [quantity, setQuantity] = useState(1);

  const handleSubmit = (e) => {
    e.preventDefault();
    onCalculate(itemName, quantity);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="item">Item Name:</label>
      <input
        type="text"
        id="item"
        value={itemName}
        onChange={(e) => setItemName(e.target.value)}
        required
      />

      <label htmlFor="quantity">Quantity:</label>
      <input
        type="number"
        id="quantity"
        value={quantity}
        onChange={(e) => setQuantity(Number(e.target.value))}
        required
      />

      <button type="submit">Calculate Resources</button>
    </form>
  );
};

export default CraftingForm;
