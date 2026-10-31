import React, { useState } from 'react';

function Counter() {
  const [counter, setCounter] = useState(0)
  console.log("react counter refreshed")

  setCounter((prev)=>{prev})

  return (
    <div>
        <button onClick={() => setCounter(counter-1)}>decrement(-)</button>
        <p>{counter}</p>
        <button onClick={() => setCounter(counter+1)}>increament(+)</button>
    </div>
  )
}

export default Counter