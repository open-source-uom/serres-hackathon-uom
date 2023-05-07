import React, { useState } from 'react'



export type CellData = {
    size: number,
    bgcolor: string,
    isRemovedForHole: boolean | null,
    index: number,
    letter: string,

}

const size = 20
function Canvas({ cellsData, handleCellClick, rows, columns }: { cellsData: CellData[], holeColor: string, rows: number, columns: number, handleCellClick: (index: number) => void }) {
    //dummy data for Cells

    const maxHeight = 500
    const maxWidth = 750
    const style = {
        display: 'grid',
        gridAutoColumns: "max-content",
        gap: 0,
        gridAutoRows: "max-content",
        gridTemplateColumns: `repeat(${columns}, 1fr)`,
        gridTemplateRows: `repeat(${rows}, 1fr)`,
        maxHeight: maxHeight,
        maxWidth: maxWidth
    };
    return (
        <div style={{ display: "flex", marginTop: "1rem" }}>
            <div style={style}>

                {cellsData.map((cellData) => {
                    console.log(cellData)
                    return <span><Cell holeColor='black' size={cellData.size} key={cellData.letter + "1"} bgcolor={cellData.bgcolor} isRemovedForHole={cellData.isRemovedForHole} index={cellData.index} letter={cellData.letter} handleCellClick={(e) => console.log("nothing")
                    } /></span>
                })}
            </div>
        </div>
    )
}


const supportedLetters = ["F", "I", "L", "N", "P", "T", "U", "V", "W", "X", "Y", "Z"]
const letterColors = [
    "#001fc4",
    "#9c1516",
    "#efee29",
    "#e719e2",
    "#07d4f3",
    "#8a8a8a",
    "#00e53f",
    "#f19a05",
    "#d5d5d5",
    "#2097b8",
    "#b82082",
    "#ff0011",
]

export function Cell({ size = 20, bgcolor = "white", isRemovedForHole, holeColor, letter, index, handleCellClick }: CellData & { holeColor: string, handleCellClick: (index: number) => void }) {
    const [isRemoved, setIsRemoved] = useState<boolean | null>(isRemovedForHole)

    let the_index = -1;
    for (let i = 0; i < supportedLetters.length; i++) {
        if (letter === supportedLetters[i]) {
            console.log("letter is: ", letter, "and color is: ", letterColors[i])
            the_index = i;
            break;
        }
    }

    let theBgColorIfLetter;
    if (index === -1) {
        theBgColorIfLetter = 'white'
    } else {
        theBgColorIfLetter = letterColors[the_index]
    }

    // const theBgColorIfLetter = index === -1 ? 'white' : supportedLetters[the_index]
    // console.log("This is: ", letter, "painted with color: ", theBgColorIfLetter)
    return (
        <div style={{
            fontSize: size / 2,
            width: size,
            height: size,
            display: "flex",
            flexDirection: "row",
            alignItems: "center",
            justifyContent: "center",
            border: `1px solid ${isRemoved ? "red" : "black"}`,
            backgroundColor: `${isRemoved ? holeColor : theBgColorIfLetter}`
        }} onClick={(e) => {
            setIsRemoved(prev => !prev)
            handleCellClick(index)
        }}>{letter}</div>
    )
}


export default Canvas