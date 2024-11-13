import React, { useEffect, useRef } from 'react';
import { Network } from 'vis-network';

const TreeVisualization = ({ nodes, edges }) => {
  const networkRef = useRef(null);

  useEffect(() => {
    if (nodes.length && edges.length) {
      const container = networkRef.current;
      const data = {
        nodes: nodes,
        edges: edges,
      };
      const options = {
        layout: {
          hierarchical: {
            direction: 'UD',
            sortMethod: 'directed',
          },
        },
        nodes: {
          shape: 'box',
          color: '#6BAED6',
        },
        edges: {
          color: '#848484',
        },
      };
      new Network(container, data, options);
    }
  }, [nodes, edges]);

  return <div ref={networkRef} style={{ height: '500px' }}></div>;
};

export default TreeVisualization;
