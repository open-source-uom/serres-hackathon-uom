import React from 'react';

const ColorizedCanvas = ({ shapes, canvasWidth, canvasHeight }) => {
    const getColor = (shapeIndex) => {
        const hue = shapeIndex * 30 % 360;
        return `hsl(${hue}, 70%, 50%)`;
    };

    return (
        <div style={{ position: 'relative', width: canvasWidth, height: canvasHeight }}>
            {shapes.map((shape, i) => (
                <div
                    key={i}
                    style={{
                        position: 'absolute',
                        left: shape.position.x,
                        top: shape.position.y,
                        width: shape.size.width,
                        height: shape.size.height,
                        background: getColor(i),
                    }}
                />
            ))}
        </div>
    );
};

export default ColorizedCanvas;
