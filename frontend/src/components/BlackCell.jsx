import React from 'react';

const BlackCell = ({ size }) => {
    const style = {
        width: size,
        height: size,
        backRoundColor: 'black',
    };
    return <div style={style}></div>;
};

export default BlackCell;