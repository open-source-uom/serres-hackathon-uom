import React from 'react';

const Cell = () => {
    const size = useStore(state=>state.size)


    const style = {
        width: size,
        height: size,
        border: '1px solid black',
    };
    return <div style={style}></div>;
};

export default Cell;