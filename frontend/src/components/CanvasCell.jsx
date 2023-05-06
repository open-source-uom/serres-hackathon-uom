import React, { useState } from 'react'
import useStore from "../store/store.js";

const isHole = (letter) => letter === "H"

function CanvasCell({letter,color,index}) {
    const [isRemovedForHole,setIsRemovedForHole] = useState(false)
    const positions = useStore(state=>state.positions)
    const setPositions = useStore(state=>state.setPositions)
    const pixels = useStore(state=>state.pixels)

    const handleClicked = (e) => {
        setIsRemovedForHole(prev=>!prev)
        positions.push(index)
        setPositions(positions)
    }
    
  const style = {
        width: pixels,
        height: pixels,
        border: '1px solid black',
        backgroundColor:`${isRemovedForHole ? "black" : color}`
    };
    return <div style={style} onClick={handleClicked}>
        {!isRemovedForHole && letter}
    </div>;
}

export default CanvasCell