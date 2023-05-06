import React, { useState } from 'react';
import Cell from './Cell';

const Canvas = () => {
    const [width, setWidth] = useState(10);
    const [height, setHeight] = useState(10);
    const [holes, setHoles] = useState([]);

    const style = {
        display: 'grid',
        gridTemplateColumns: `repeat(${width}, 1fr)`,
        gridTemplateRows: `repeat(${height}, 1fr)`,
    };

    const handleClick = (x, y) => {
        setHoles((prevHoles) => [...prevHoles, { x, y }]);
    };

    // Create a 2D array of cells
    const cells = [];
    for (let i = 0; i < height; i++) {
        const row = [];
        for (let j = 0; j < width; j++) {
            const isHole = holes.some((hole) => hole.x === j && hole.y === i);
            row.push(
                <Cell key={`${j},${i}`} size={20} isHole={isHole} onClick={() => handleClick(j, i)} />
            );
        }
        cells.push(row);
    }

    return (
        <div>
            <label>
                Width:{' '}
                <input type="number" value={width} onChange={(e) => setWidth(Number(e.target.value))} />
            </label>
            <br />
            <label>
                Height:{' '}
                <input type="number" value={height} onChange={(e) => setHeight(Number(e.target.value))} />
            </label>
            <div style={style}>{cells}</div>
        </div>
    );
};

export default Canvas;
