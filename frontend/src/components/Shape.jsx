import React from 'react';

const Shape = ({ vectors, size }) => {
    const style = {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        width: size * (Math.max(...vectors.map(([x]) => x)) + 1),
        height: size * (Math.max(...vectors.map(([, y]) => y)) + 1),
        backgroundColor: 'lightgray',
    };

    return (
        <div style={style}>
            {vectors.map(([x, y]) => (
                <div
                    key={`${x},${y}`}
                    style={{
                        position: 'absolute',
                        left: x * size,
                        top: y * size,
                        width: size,
                        height: size,
                        backgroundColor: 'black',
                    }}
                />
            ))}
        </div>
    );
};

export default Shape;
