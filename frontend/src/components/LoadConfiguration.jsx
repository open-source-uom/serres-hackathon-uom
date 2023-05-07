
const LoadConfiguration = ({ onClick }) => {

    const handleLoad = (event) => {
        const file = event.target.files?.[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                const text = e.target?.result;

                if (typeof text === "string") {
                    const json = JSON.parse(text.toString());
                    console.log(json);
                    onClick(text);
                } else if (typeof text === "ArrayBuffer") {
                    const text = new TextDecoder().decode(text)
                    onClick(text);
                }

            };
            reader.readAsText(file);
        }
    };

    return (
        <div>
            <label>
                Load Configuration:{' '}
                <br />
                <input type="file" accept="application/json" onChange={handleLoad} />
            </label>
        </div>
    );
}

export default LoadConfiguration;