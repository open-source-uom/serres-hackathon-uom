import React, { useState } from 'react';
import Canvas from './components/Canvas';
import LetterSelection from './components/LetterSelection';
import Rotate from './components/Rotate';
import Shape from './components/Shape';
import Configuration from './components/Configuration';
import Timer from './components/Timer';
import ColorizedCanvas from './components/ColorizedCanvas';
import UniqueSolutions from './components/UniqueSolutions';
import Results from './components/Results';
import useStore from "./store/store.js";
import InputDimensions from './components/InputDimensions';

const dummy_colorized = [
            [
                {
                    id: 1,
                    position: { x: 10, y: 10 },
                    size: { width: 50, height: 50 },
                },
                {
                    id: 2,
                    position: { x: 70, y: 10 },
                    size: { width: 30, height: 80 },
                },
            ],
            [
                {
                    id: 1,
                    position: { x: 10, y: 10 },
                    size: { width: 50, height: 50 },
                },
                {
                    id: 2,
                    position: { x: 70, y: 10 },
                    size: { width: 30, height: 80 },
                },
                {
                    id: 3,
                    position: { x: 140, y: 10 },
                    size: { width: 60, height: 60 },
                },
            ],
        ];


const App = () => {
    
    const [rotateShapes, setRotateShapes] = useState(false);
    const [flipShapes, setFlipShapes] = useState(false);
    const [configuration, setConfiguration] = useState('');
    const [elapsedTime, setElapsedTime] = useState(0);
    const [uniqueSolutions, setUniqueSolutions] = useState(0);
    const [results, setResults] = useState([]);
    const rows = useStore(state=>state.rows)
    const columns = useStore(state=>state.columns)

    const handleSolveClick = () => {
        // Perform solver logic here and update state with results
        const dummyResults = [
            [
                {
                    id: 1,
                    position: { x: 10, y: 10 },
                    size: { width: 50, height: 50 },
                },
                {
                    id: 2,
                    position: { x: 70, y: 10 },
                    size: { width: 30, height: 80 },
                },
            ],
            [
                {
                    id: 1,
                    position: { x: 10, y: 10 },
                    size: { width: 50, height: 50 },
                },
                {
                    id: 2,
                    position: { x: 70, y: 10 },
                    size: { width: 30, height: 80 },
                },
                {
                    id: 3,
                    position: { x: 140, y: 10 },
                    size: { width: 60, height: 60 },
                },
            ],
        ];
        setResults(dummyResults);
    }

    return (
        <div width="100vw" >
            <h1>Canvas Solver App</h1>
            <div>
                <InputDimensions />
                <div style={{width:"600px",height:"2px",backgroundColor:"green",margin:"1rem"}}></div>
                {/* <Cell value={cells} onChange={setCells} /> */}
                <Canvas
                    width={rows}
                    height={rows}
                />
                <LetterSelection />
                <Rotate
                    rotate={rotateShapes}
                    flip={flipShapes}
                    onRotateChange={setRotateShapes}
                    onFlipChange={setFlipShapes}
                />
                <Configuration value={configuration} onChange={setConfiguration} />
                <Timer time={elapsedTime} />
                <button onClick={handleSolveClick}>Solve</button>
                <Results results={results} />
            </div>
        </div>
    );
};

export default App;
