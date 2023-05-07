import React, { useState } from 'react'
import useStore from "../store/store.js";

const isHole = (letter) => letter === "H"

const letterColors = {
    F: "#001fc4",
    I: "#9c1516",
    L: "#efee29",
    N: "#e719e2",
    P: "#07d4f3",
    T: "#8a8a8a",
    U: "#00e53f",
    V: "#f19a05",
    W: "#d5d5d5",
    X: "#2097b8",
    Y: "#b82082",
    Z: "#ff0011",
};

const getColorOfLetter = (letter) => {
    if (isHole(letter)) {
        return "black"
    }
    return letterColors[letter]
}


function CanvasCell({letter,color,index}) {
    const [isRemovedForHole,setIsRemovedForHole] = useState(false)
    const positions = useStore(state=>state.positions)
    const setPositions = useStore(state=>state.setPositions)
    const pixels = useStore(state=>state.pixels)
    // console.log("RENDERED CELLS")
    const handleClicked = (e) => {
        setIsRemovedForHole(prev=>!prev)
        positions.push(index)
        setPositions(positions)
    }
    const colorOfLetter = getColorOfLetter(letter)
    console.log("Letter is:",colorOfLetter)
  const style = {
        width: pixels,
        height: pixels,
        border: '1px solid black',
        borderRight: `3px solid ${getColorOfLetter(letter)}`,
        backgroundColor:`${isRemovedForHole ? "black" : color}`
    };
    return <div style={style} onClick={handleClicked}>
        {!isRemovedForHole && letter}
    </div>;
}

export default CanvasCell