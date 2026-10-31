import React, { useState } from 'react'

function ShowHide() {
    const [show, setShow] = useState(true);

  return (
    <>
        <button onClick={() => setShow(!show)}>{show ? 'Hide' : 'Show'}</button>
        {show && <p>Free Wi-Fi, breakfast, and parking.</p>}
    </>
  )
}

export default ShowHide