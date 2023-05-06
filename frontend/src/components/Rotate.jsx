import React, { useState } from 'react';

const Rotate = () => {
    const [isRotated, setIsRotated] = useState(false);

    const handleToggle = () => {
        setIsRotated((prev) => !prev);
    };

    return (
        <div>
            <label>
                Rotate shapes:{' '}
                <input type="checkbox" checked={isRotated} onChange={handleToggle} />
            </label>
        </div>
    );
};

export default Rotate;
