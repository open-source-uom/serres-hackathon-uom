import React, { useState, useEffect, useRef } from 'react';

const Timer = () => {
    const [time, setTime] = useState(0);
    const [isRunning, setIsRunning] = useState(false);
    const intervalRef = useRef(null);

    useEffect(() => {
        if (isRunning) {
            intervalRef.current = setInterval(() => {
                setTime((prevTime) => prevTime + 1);
            }, 1000);
        } else {
            clearInterval(intervalRef.current);
        }
        return () => clearInterval(intervalRef.current);
    }, [isRunning]);

    const handleStart = () => setIsRunning(true);
    const handleStop = () => setIsRunning(false);
    const handleReset = () => setTime(0);

    const formatTime = (time) => {
        const minutes = Math.floor(time / 60);
        const seconds = time % 60;
        return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    };

    return (
        <div>
            <h3>Timer</h3>
            <div>{formatTime(time)}</div>
            <button onClick={handleStart} disabled={isRunning}>
                Start
            </button>
            <button onClick={handleStop} disabled={!isRunning}>
                Stop
            </button>
            <button onClick={handleReset}>Reset</button>
        </div>
    );
};

export default Timer;

