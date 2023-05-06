import {create} from "zustand"


const useStore = create()(set => ({
    rows: 10,
    columns: 10,
    pixels : 25,
    positions: [],
    canvas: [],
    lettersSelected: [],
    isRotated: false,
    isFetched: false,
    //xreiazetai allagh
    config: {
        rows: 10,
        columns: 10,
        positions: [],
        lettersSelected: [],
        isRotated: false,
    },
    setRows: (the_rows) => set((state) => {
        console.log(the_rows)
        console.log(state)
        return { ...state, rows: the_rows, canvas: Array(state.rows * state.columns).fill({ letter: "Α", color: "grey" }) }
    }),
    // αυτό θα χρειαστεί να αλλάξει
    setColumns: (the_columns) => set((state) =>

        ({ ...state, columns: the_columns, canvas: Array(state.rows * state.columns).fill({ letter: "B", color: "grey" }) })),
    setPixels: (the_pixels) => set((state) => ({ ...state, pixels: the_pixels })),
    setCanvas: (arr) => set(state => { return { canvas: arr, ...state } }),
    setSelectedLetters: (arr) => set(state => {
        return { lettersSelected: arr, ...state }
    }),
    addLetter: (letter) => set(state => {
        state.lettersSelected.push(letter)
        const my_arr = [...state.lettersSelected]
        return { lettersSelected: my_arr, ...state }
    }),
    setConfig: (config) => set(state => {
        return { ...state, config: {...config} }
    }),
    setIsRotated: (isRotated) => set(state => {
        return { ...state, isRotated: isRotated }
    }),
    setPositions: (positions) => set(state => {
        return { positions: positions, ...state }
    }),
    setIsFetched: (isFetched) => set(state => {
        return { isFetched: isFetched, ...state }
    }),
    getRows: () => {
        return useStore.getState().rows
    },
    getColumns: () => {
        return useStore.getState().columns
    },
    getPixels: () => {
        return useStore.getState().pixels
    },
    getLettersSelected: () => {
        return useStore.getState().lettersSelected
    },
    getIsRotated: () => {
        return useStore.getState().isRotated
    },
    getPositions: () => {
        return useStore.getState().positions
    },
}))

export default useStore