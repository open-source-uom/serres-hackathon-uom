import React from 'react'

function SolveButton({ onClick }: { onClick: (e: any) => void }) {
  return (
    <button onClick={onClick} style={{ marginTop: "1rem" }}>Solve Problem</button>
  )
}

export default SolveButton