import React, { useState } from 'react'

const isHole = (letter) => letter === "H"


function CanvasCell({letter,color,size,index}) {
const [isRemovedForHole,setIsRemovedForHole] = useState(false)

    
  const style = {
        width: size,
        height: size,
        border: '1px solid black',
        backgroundColor:`${isRemovedForHole ? "black" : color}`
    };
    return <div style={style} onClick={(e)=>setIsRemovedForHole(prev=>!prev)}>
        {!isRemovedForHole && letter}
    </div>;
}

export default CanvasCell