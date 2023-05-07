

const SaveConfiguration = ({ configurationText }) => {


    const handleSave = async () => {
        const text = 'Hello, world!';
        const file = new Blob([configurationText], { type: 'text/plain' });

        // save the file using FileSaver API
        if (window.navigator.msSaveOrOpenBlob) {
            window.navigator.msSaveOrOpenBlob(file, 'hello.txt');
        } else {
            const a = document.createElement('a');
            const url = URL.createObjectURL(file);
            a.href = url;
            a.download = 'config.json';
            document.body.appendChild(a);
            a.click();
            setTimeout(() => {
                document.body.removeChild(a);
                window.URL.revokeObjectURL(url);
            }, 0);
        }
    }
    // save the file using FileSaver API
    // if (window.navigator.) {
    //     window.navigator.msSaveOrOpenBlob(file, 'hello.txt');
    // } else {
    //     const a = document.createElement('a');
    //     const url = URL.createObjectURL(file);
    //     a.href = url;
    //     a.download = 'hello.txt';
    //     document.body.appendChild(a);
    //     a.click();
    //     setTimeout(() => {
    //         document.body.removeChild(a);
    //         window.URL.revokeObjectURL(url);
    //     }, 0); 

    return (
        <div>
            <h3>Configuration:</h3>
            <button onClick={handleSave}>Save Configuration</button>
            <br />
        </div>
    )
}

export default SaveConfiguration