import React from "react";
import useStore from "../store/store";

function LetterSelection() {
  const lettersSelected = useStore((state) => state.lettersSelected);
  const setSelectedLetters = useStore((state) => state.setSelectedLetters);
  const letters = ["F", "I", "L", "N", "P", "T", "U", "V", "W", "X", "Y", "Z"];

  const letterColors = {
    F: "#001fc4",
    I: "#9c1516",
    L: "#efee29",
    N: "#e719e2",
    P: "#07d4f3",
    T: "#8a8a8a",
    U: "#00e53f",
    V: "#f19a05",
    W: "#d5d5d5",
    X: "#2097b8",
    Y: "#b82082",
    Z: "#ff0011",
  };
  console.log(lettersSelected)

  const handleLetterClick = (letter) => {
    lettersSelected.push(letter)
    setSelectedLetters([...lettersSelected, letter]);
  };

  const handleSelectAll = () => {
    lettersSelected.push(...letters)
    setSelectedLetters([...lettersSelected, ...letters]);
  }

  return (
    <div>
      {letters.map((letter) => (
        <button key={letter} style={{ backgroundColor: letterColors[letter] }} onClick={(e) => handleLetterClick(letter)}>
          {letter}
        </button>
      ))}
      <br />
      {lettersSelected.map((letter) => (
        <span key={letter} style={{ backgroundColor: letterColors[letter] }}>
          {letter}
        </span>
      ))}
      <button onClick={handleSelectAll}>Select All</button>
    </div>
  );
}

export default LetterSelection;
