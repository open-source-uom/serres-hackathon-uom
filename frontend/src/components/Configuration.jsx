import React, { useState } from 'react';

const Configuration = () => {
    const [config, setConfig] = useState(null);

    const handleSave = () => {
        const json = JSON.stringify(config);
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
            <label>
                Load Configuration:{' '}
                <input type="file" accept="application/json" onChange={handleLoad} />
            </label>
            <pre>{config && JSON.stringify(config, null, 2)}</pre>
        </div>
    );
};

export default Configuration;
