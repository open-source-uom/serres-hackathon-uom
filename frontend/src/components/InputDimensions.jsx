import React from 'react'
import useStore from '../store/store'

function InputDimensions() {

    const rows = useStore(state=>state.rows)
    const columns = useStore(state=>state.columns)
    const setRows = useStore(state=>state.setRows)
    const setColumns = useStore(state=>state.setColumns)
    const pixels = useStore(state=>state.pixels)
    const setPixels = useStore(state=>state.setPixels)

  return (
    <div>
        <label>
                Pixels:{' '}
                <input type="number" step="5" min="25" max="50" value={pixels} onChange={(e) => setPixels(Number(e.target.value))} />
        </label>
        <br />
        <br />
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