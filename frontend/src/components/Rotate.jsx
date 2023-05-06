import React, { useState } from 'react';
import useStore from "../store/store.js";

const Rotate = () => {
    const [isChecked, setIsChecked] = useState(false);
    const isRotated = useStore(state => state.isRotated);
    const setIsRotated = useStore(state => state.setIsRotated);

    //mhn to aggiksei kapoios, leitourgei for some reason, idk einai 12 to bradu pleon
    const handleToggle = () => {
        setIsChecked(!isChecked);
        setIsRotated(!isChecked);
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
