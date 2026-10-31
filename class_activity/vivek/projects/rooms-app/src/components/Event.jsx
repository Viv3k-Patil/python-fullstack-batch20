function BookButton() {
  function handleClick() {
    alert("Room booked! 🎉")
  }

  return <button 
        onClick={handleClick}
        onMouseOver={(e) => console.log(e.clientX, e.clientY)}
    >Book Now</button>
}

export default BookButton