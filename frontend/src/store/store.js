import { create } from "zustand"


const useStore = create()(set => ({
    rows: 10,
    columns: 10,
    canvas: [],
    lettersSelected: [],
    setRows: (the_rows) => set((state) => {
        console.log(the_rows)
        console.log(state)
        return { ...state, rows: the_rows, canvas: Array(state.rows * state.columns).fill({ letter: "Α", color: "grey" }) }
    }),
    // αυτό θα χρειαστεί να αλλάξει
    setColumns: (the_columns) => set((state) =>

        ({ ...state, columns: the_columns, canvas: Array(state.rows * state.columns).fill({ letter: "Α", color: "grey" }) })),
    setCanvas: (arr) => set(state => { return { canvas: arr, ...state } }),
    setSelectedLetters: (arr) => set(state => {
        console.log("Was called")
        console.log(state)
        console.log(arr)
        return { lettersSelected: arr, ...state }
    }),
    addLetter: (letter) => set(state => {
        console.log("addLetter")
        console.log(state)
        console.log("Letter: ", letter, state.lettersSelected)
        state.lettersSelected.push(letter)
        const my_arr = [...state.lettersSelected]
        console.log("MY NEW ARRAY: ", my_arr)
        // const my_arr = [...state.lettersSelected, letter]
        return { lettersSelected: my_arr, ...state }
    })
}))

export default useStore