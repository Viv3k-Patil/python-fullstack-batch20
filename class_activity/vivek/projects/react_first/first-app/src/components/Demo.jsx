import React, { useEffect, useState } from 'react'

function Demo() {
    const [counter, setCounter] = useState(0)

    useEffect(() => {
        console.log("component re-render")
    },[counter])


  return (
    <div>
        <p>{counter}</p>
        <button onClick={() => setCounter(counter+1)}>+</button>
    </div>
  )
}

export default Demo