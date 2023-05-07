import React from 'react'

function ShowSelectedLetters({ letterList }: { letterList: string[] }) {
    return (
        <>
            <h3>Selected Letters:</h3>
            {letterList.map((letter) => {
                return <span style={{ fontSize: "1.2rem" }}>{letter}-</span>
            })}
        </>
    )
}

export default ShowSelectedLetters