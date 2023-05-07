import React from 'react';
import CanvasCell from './CanvasCell';

const letterColors = {
    F: '#001fc4',
    I: '#9c1516',
    L: '#efee29',
    N: '#e719e2',
    P: '#07d4f3',
    T: '#8a8a8a',
    U: '#00e53f',
    V: '#f19a05',
    W: '#d5d5d5',
    X: '#2097b8',
    Y: '#b82082',
    Z: '#ff0011',
};

const ColorizedCanvas = ({ solution, rows, columns }) => {
    const canvasArr = [];

    for (let row = 0; row < solution.length / rows; row++) {
        for (let col = 0; col < rows; col++) {
            const index = row * rows + col;
            const letter = solution[index];
            const color = letterColors[letter];
            canvasArr.push({ letter, color, row, col });
        }
    }
    return (
        <div style={{ display: 'grid', gridTemplateColumns: `repeat(${columns}, 1fr)`, gap: 0 }}>
            {canvasArr.map((obj, pos) => (
                <CanvasCell key={pos} index={pos} {...obj} size="20" />
            ))}
        </div>
    );
};

export default ColorizedCanvas;
