import React from 'react';

const Results = ({ results }) => {
    const resultsText = results.map((result) => {
        return result.map((shape) => {
            return `Shape ${shape.id}: x=${shape.position.x}, y=${shape.position.y}, w=${shape.size.width}, h=${shape.size.height}\n`;
        }).join('');
    }).join('\n');

    const handleDownload = () => {
        const element = document.createElement('a');
        const file = new Blob([resultsText], {type: 'text/plain'});
        element.href = URL.createObjectURL(file);
        element.download = 'results.txt';
        document.body.appendChild(element);
        element.click();
    }

    return (
        <div>
            <h2>Results:</h2>
            <pre>{resultsText}</pre>
            <button onClick={handleDownload}>Download Results</button>
        </div>
    );
};

export default Results;
