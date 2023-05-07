import { Cell } from "./Canvas";

type Props = {
    rows: number,
    columns: number,
    colorForHoles: string,
    cellSize: number,
    handleCellClick: (index: number) => void
}

function BlankCanvas({ rows, columns, colorForHoles, cellSize, handleCellClick }: Props) {
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
                {Array.from(Array(rows * columns).keys()).map((index) => { return <Cell holeColor="black" size={cellSize} bgcolor={"white"} isRemovedForHole={false} index={index} letter={""} handleCellClick={handleCellClick} /> })}
                {/* {cellsData.map((cellData) => { return <Cell size={maxHeight / rows} bgcolor={cellData.bgcolor} isRemovedForHole={cellData.isRemovedForHole} index={cellData.index} letter={cellData.letter} /> })} */}
            </div>
        </div>
    )
}

export default BlankCanvas