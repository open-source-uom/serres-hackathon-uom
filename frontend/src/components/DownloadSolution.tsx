
const DownloadSolution = ({ results }: { results: any }) => {

    const handleDownload = () => {
        const element = document.createElement("a");
        const file = new Blob([JSON.stringify(results)], { type: 'application/json' });
        element.href = URL.createObjectURL(file);
        element.download = "results.json";
        document.body.appendChild(element); // Required for this to work in FireFox
        element.click();
    }

    return (
        <div>
            <button onClick={handleDownload}>Download Results</button>
        </div>
    );
}

export default DownloadSolution;