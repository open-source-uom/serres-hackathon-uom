import React from 'react'
import Canvas from './Canvas';

type CellData = {
    size: number,
    bgcolor: string,
    isRemovedForHole: boolean,
    index: number,
    letter: string,
}
const size = 20;

function DisplaySolution({ cellsData, rows, columns }: { cellsData: CellData[], rows: number, columns: number }) {

    return (
        <div style={{ padding: "1rem" }}>
            <Canvas cellsData={cellsData} holeColor='yellow' handleCellClick={(e) => console.log("nothing")} columns={columns} rows={rows} />
        </div >
    )
}

export default DisplaySolution