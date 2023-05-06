import useStore from "../store/store.js";
import {useEffect, useReducer} from "react";
import error from "eslint-plugin-react/lib/util/error.js";


const initialState = {
    data: null,
    isLoading: false,
    error: null,
};

const reducer = (state, action) => {
    switch (action.type) {
        case 'FETCH_START':
            return {
                ...state,
                isLoading: true,
                error: null,
            };
        case 'FETCH_SUCCESS':
            return {
                ...state,
                isLoading: false,
                data: action.payload,
            };
        case 'FETCH_ERROR':
            return {
                ...state,
                isLoading: false,
                error: action.payload,
            };
        default:
            throw new Error(`Unhandled action type: ${action.type}`);
    }
};

const initializer = (initialState) => {
    return {data: "Hello world",
        isLoading: true,
        error: "haaa",}
};

//data:{
//             rows: getRows(),
//             columns: getColumns(),
//             positions: getPositions(),
//             lettersSelected: getLettersSelected(),
//             isRotated: getIsRotated()
//         }

function useFetchSolution(data,shouldFetch){
    const [state,dispatch] = useReducer(reducer,initialState,initializer)
    useEffect(() => {
        let ignore = false;
        const fetchSolution = async () => {
            // const response = await fetch("http://localhost:5000/solution")
            // const data = await response.json()
            // console.log(data)
            // useStore.setState({positions: data.positions, isFetched: true})
            if(ignore) return
            console.log('FETCHING')
            dispatch({ type: 'FETCH_START' });
            try{
                const body = JSON.stringify(data)


                const awaitVal = await new Promise((resolve, reject) => {
                    setTimeout(() => {
                        resolve("FFLLΙ YFFLΙ ΥFTLΙ ΥΥTLΙ ΥΤΤΤΙ")
                    }, 2000)
                })
                dispatch({ type: 'FETCH_SUCCESS', payload: awaitVal });
            }catch{
                dispatch({ type: 'FETCH_ERROR', payload: error });
            }

            }
            if(shouldFetch){
                fetchSolution()
            }
        return () => { ignore = true; };

    },[shouldFetch])
    return state
}

export default useFetchSolution