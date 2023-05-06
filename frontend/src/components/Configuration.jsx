import React, { useState } from 'react';
import useStore from "../store/store";

const Configuration = () => {
    const [config, setConfig] = useStore(state=>[state.config, state.setConfig])
    const getRows = useStore(state=>state.getRows)
    const getColumns = useStore(state=>state.getColumns)
    const getLettersSelected = useStore(state=>state.getLettersSelected)
    const getIsRotated = useStore(state=>state.getIsRotated)
    const getPositions = useStore(state=>state.getPositions)

    const handleSave = () => {
        const json = JSON.stringify(
            {
                rows: getRows(),
                columns: getColumns(),
                positions: getPositions(),
                lettersSelected: getLettersSelected(),
                isRotated: getIsRotated()
            }
        );
        const blob = new Blob([json], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'configuration.json';
        a.click();
        URL.revokeObjectURL(url);
    };

    const handleLoad = (e) => {
        const file = e.target.files[0];
        const reader = new FileReader();
        reader.onload = (event) => {
            const json = event.target.result;
            setConfig(JSON.parse(json));
        };
        reader.readAsText(file);
    };

    return (
        <div>
            <h3>Configuration</h3>
            <button onClick={handleSave}>Save Configuration</button>
            <br />
            <label>
                Load Configuration:{' '}
                <input type="file" accept="application/json" onChange={handleLoad} />
            </label>
        </div>
    );
};

export default Configuration;
