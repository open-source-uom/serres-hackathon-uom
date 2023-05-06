import React from 'react'
import useStore from '../store/store'

function InputDimensions() {

const rows = useStore(state=>state.rows)
const columns = useStore(state=>state.columns)
const setRows = useStore(state=>state.setRows)
const setColumns = useStore(state=>state.setColumns)
  return (
    <div>
        <label>
                Rows:{' '}
                <input type="number" value={rows} onChange={(e) => setRows(Number(e.target.value))} />
        </label>
        <br />
        <br />
        <label>
                Columns:{' '}
                <input type="number" value={columns} onChange={(e) => setColumns(Number(e.target.value))} />
        </label>
    </div>
  )
}

export default InputDimensions