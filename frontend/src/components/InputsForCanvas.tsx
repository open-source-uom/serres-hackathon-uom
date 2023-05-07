import React,{useState} from 'react'

type Props = {
    rows:number,
    columns:number,
    pixels:number,
    setRows:React.Dispatch<React.SetStateAction<number>>,
    setColumns:React.Dispatch<React.SetStateAction<number>>,
    setPixels:React.Dispatch<React.SetStateAction<number>>,
}


function InputsForCanvas({rows,columns,pixels,setRows,setColumns,setPixels}:Props) {
    // const [rows, setRows] = useState(1)
    // const [columns, setColumns] = useState(1)
    // const [pixels,setPixels] = useState(20)
  
    return (
    <div>
        <label>
                Rows:{' '}
                <input type="number" min="1" value={rows} onChange={(e) => setRows(Number(e.target.value))} />
        </label>
        <br />
        <br />
        <label>
                Columns:{' '}
                <input type="number" min="1" value={columns} onChange={(e) => setColumns(Number(e.target.value))} />
        </label>
        <br />
        <br />
        <label>
                Pixels:{' '}
                <input type="number" step="5" min="20" max="50" value={pixels} onChange={(e) => setPixels(Number(e.target.value))} />
        </label>
    </div>
  )
}

export default InputsForCanvas