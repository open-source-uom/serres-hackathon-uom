import React, { useState } from 'react';
import useStore from "../store/store.js";

const Rotate = () => {
    const [isChecked, setIsChecked] = useState(false);
    const isRotated = useStore(state => state.isRotated);
    const setIsRotated = useStore(state => state.setIsRotated);

    const handleToggle = () => {
        setIsChecked(!isChecked);
        setIsRotated(isChecked);
        console.log("isRotated: ", isRotated);
    };

    return (
        <div>
            <label>
                Rotate shapes:{' '}
                <input type="checkbox" checked={isChecked} onChange={handleToggle} />
            </label>
        </div>
    );
};

export default Rotate;
