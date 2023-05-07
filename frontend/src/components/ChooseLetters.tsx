import React, { useState } from 'react'

function ChooseLetters({ letterList, setLetterList }: { letterList: string[], setLetterList: React.Dispatch<React.SetStateAction<string[]>> }) {
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

    const handleLetterClick = (letter: string) => {
        setLetterList(prev => [...prev, letter])
    }



    return (
        <div style={{ margin: "1rem 0rem" }}>ChooseLetters:
            <br />
            <div style={{ display: "flex", columnGap: "0.5rem" }}>

                {supportedLetters.map((letter, index) => {
                    return <button style={{ color: letterColors[index] }} onClick={(e) => handleLetterClick(letter)}>{letter}</button>
                })}
            </div>
        </div>
    )
}

export default ChooseLetters