import React, { useState } from 'react';
import useStore from '../store/store';
import CanvasCell from './CanvasCell';

const Canvas = () => {
    const rows = useStore(state=>state.rows)
    const columns = useStore(state=>state.columns)
    // console.log(rows,columns,canvasArr)
    const canvasArr = useStore(state=> state.canvas)
    const setCanvas = useStore(state=>state.setCanvas)



    const [holes, setHoles] = useState([]);

        const maxHeight = 500
        const maxWidth = 750
    const style = {
        display: 'grid',
        gridAutoColumns:"max-content",
        gap: 0,
        gridAutoRows:"max-content",
        gridTemplateColumns: `repeat(${columns}, 1fr)`,
        gridTemplateRows: `repeat(${rows}, 1fr)`,
        maxHeight:maxHeight,
        maxWidth:maxWidth
    };

    const handleCanvasChange = (index,letter,color) => {
        setCanvas((prevCanvas) => {
            let newCanvas = [...prevCanvas]
            newCanvas[index] = {letter,color}
            return newCanvas
        });
    };

    // Create a 2D array of cells
    // const cells = [];
    
    // all_elems.push({letter:"A",color:"red"})
    // .push({letter:"A",color:"red"})
    
    let empty_char = 'E'
    return (
        <div>
            
            <div style={style}>
                {canvasArr.map((obj,pos)=><CanvasCell key={pos} index={pos} {...obj} size="20" onChange={handleCanvasChange} />)}
            </div>
        </div>
    );
};

export default Canvas;
