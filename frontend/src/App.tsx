import { useState } from 'react'
import Title from './components/Title'
import InputsForCanvas from './components/InputsForCanvas'
import Canvas from './components/Canvas'
import SolveButton from './components/SolveButton'
import DisplaySolution from './components/DisplaySolution'
import BlankCanvas from './components/BlankCanvas'
import ChooseLetters from './components/ChooseLetters'
import ShowSelectedLetters from './components/ShowSelectedLetters'
import SaveConfiguration from './components/SaveConfiguration.jsx'
import DownloadSolutions from './components/DownloadSolutions'
import LoadConfiguration from './components/LoadConfiguration'

type CellData = {
  size: number,
  bgcolor: string,
  isRemovedForHole: boolean,
  index: number,
  letter: string,
}

let api_port = "8000"
let api_route = "solve"
function App() {
  const [rows, setRows] = useState(5)
  const [columns, setColumns] = useState(5)
  const [pixels, setPixels] = useState(30)
  const [letterList, setLetterList] = useState<string[]>([])
  const [holes, setHoles] = useState<number[]>([])
  const [result, setResult] = useState<CellData[]>([])
  const [multipleResults, setResults] = useState<CellData[][]>([])
  const [time, setTime] = useState<string>("")
  const [isRotated, setIsRotated] = useState<boolean>(false)
  const [downloadSolutions, setDownloadSolutions] = useState<string[]>([])
  const handleCellClick = (index: number) => {
    console.log("cell clicked", index)
    if (holes.includes(index)) {
      setHoles(holes.filter((hole) => hole !== index))
    } else {
      setHoles([...holes, index])
    }
  }

  const configData = {
    rows: rows,
    columns: columns,
    letterList: letterList,
    holes: holes,
    isRotated: isRotated
  }

  const configString = JSON.stringify(configData)





  const sendRequest = async () => {
    console.log("send request")
    // convert index of holes to x,y
    const x_values = holes.map((hole) => hole % columns)
    const y_values = holes.map((hole) => Math.floor(hole / columns))
    if (x_values.length !== y_values.length) {
      throw Error("x_values.length !== y_values.length")
    }
    let holes_coordinates: number[][] = []
    for (let i = 0; i < x_values.length; i++) {
      holes_coordinates.push([x_values[i], y_values[i]])
    }

    let total_result: any[] = []
    //console.log("holes_coordinates", holes_coordinates)
    const data = {
      rows: rows,
      columns: columns,
      letterList: letterList,
      holes,
      isRotated: isRotated
    }
    console.log("data", data)
    const response = fetch(`http://localhost:${api_port}/${api_route}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        'Access-Control-Allow-Origin': '*'
      },
      body: JSON.stringify(data),
    }).then((response) => {
      return response.json()
    }).then((res: any) => {
      console.log(res)
      const time = res.time as string;
      const solutions = res.solutions as string[];
      total_result = solutions.map((solution: string) => {
        return Array.from(solution.replace(/ /g, "")).map((letter, index) => {
          return {
            size: pixels,
            bgcolor: "red",
            isRemovedForHole: false,
            index: index,
            letter: letter
          }


        })
      })
      setDownloadSolutions(solutions)
      setResults(total_result)
      setTime(time)
    }).catch((err: any) => {
      console.log(err)
    })




    // console.log("response", response)
    // // const result = await response.json()
    // console.log(result)
    // const solution = result.solution as string;
    // const total_result = Array.from(solution.replace(/ /g, "")).map((letter, index) => {
    //   return {
    //     size: pixels,
    //     bgcolor: "red",
    //     isRemovedForHole: false,
    //     index: index,
    //     letter: letter
    //   }
    // })

    // console.log("TOTAL RESULT IS", total_result)
    setResult(total_result)

    // setTime(result.time)
    // update state with response

    // console.log("data", data)
  }

  const handleLoadConfiguration = (e: string) => {
    console.log("handleLoadConfiguration", e)
    const data = JSON.parse(e)
    setRows(data.rows)
    setColumns(data.columns)
    setLetterList(data.letterList)
    setHoles(data.holes)
    setIsRotated(data.isRotated)
  }



  return (
    <div style={{ width: "100vw", height: "100vh", justifyContent: "center", alignItems: "center", flexDirection: "column", padding: "1rem" }}>
      <Title />
      <InputsForCanvas columns={columns} pixels={pixels} rows={rows} setColumns={setColumns} setPixels={setPixels} setRows={setRows} />
      <BlankCanvas cellSize={pixels} colorForHoles='black' columns={columns} rows={rows} handleCellClick={handleCellClick} />
      <ChooseLetters letterList={letterList} setLetterList={setLetterList} />
      <ShowSelectedLetters letterList={letterList} />
      <br />
      <label style={{ marginLeft: "1rem" }}>
        Rotate Letters
        <input type="checkbox" checked={isRotated} onChange={(e) => setIsRotated(!isRotated)} />
      </label>
      <br />
      <SaveConfiguration configurationText={configString} />
      <LoadConfiguration onClick={handleLoadConfiguration} />
      <SolveButton onClick={(e) => sendRequest()} />
      <br />
      <span style={{ fontSize: "1.4rem" }}>{time && "Found Solution" + `${multipleResults.length > 1 ? "s" : ""}` + " in time: " + time + "ms"}</span>
      <br />
      {multipleResults.map((result, index) => {
        return <DisplaySolution cellsData={result} columns={columns} rows={rows} key={index} />
      })}
      <DisplaySolution cellsData={result} columns={columns} rows={rows} />
      <br />
      <DownloadSolutions results={downloadSolutions} />
      <br />
    </div>
  )
}

export default App
