import React, { useState } from 'react';
import Cell from './components/Cell';
import Canvas from './components/Canvas';
import Rotate from './components/Rotate';
import Shape from './components/Shape';
import Configuration from './components/Configuration';
import Timer from './components/Timer';
import ColorizedCanvas from './components/ColorizedCanvas';
import UniqueSolutions from './components/UniqueSolutions';
import Results from './components/Results';

const App = () => {
    const [cells, setCells] = useState(10);
    const [canvasWidth, setCanvasWidth] = useState(20);
    const [canvasHeight, setCanvasHeight] = useState(20);
    const [shapes, setShapes] = useState([]);
    const [rotateShapes, setRotateShapes] = useState(false);
    const [flipShapes, setFlipShapes] = useState(false);
    const [configuration, setConfiguration] = useState('');
    const [elapsedTime, setElapsedTime] = useState(0);
    const [colorizedShapes, setColorizedShapes] = useState([]);
    const [uniqueSolutions, setUniqueSolutions] = useState(0);
    const [results, setResults] = useState([]);

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
        <div>
            <h1>Canvas Solver App</h1>
            <div>
                <Cell value={cells} onChange={setCells} />
                <Canvas
                    width={canvasWidth}
                    height={canvasHeight}
                />
                <Rotate
                    rotate={rotateShapes}
                    flip={flipShapes}
                    onRotateChange={setRotateShapes}
                    onFlipChange={setFlipShapes}
                />
                {/*<Shape shapes={shapes} onShapesChange={setShapes} />*/}
                <Configuration value={configuration} onChange={setConfiguration} />
                <Timer time={elapsedTime} />
                <button onClick={handleSolveClick}>Solve</button>
                {/*<ColorizedCanvas shapes={colorizedShapes} />*/}
                {/*<UniqueSolutions count={uniqueSolutions} />*/}
                <Results results={results} />
            </div>
        </div>
    );
};

export default App;
