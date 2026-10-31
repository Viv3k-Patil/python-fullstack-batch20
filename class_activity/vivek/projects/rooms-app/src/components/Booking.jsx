import { useState } from "react"



function BookingList() {
  const [bookings, setBookings] = useState([])

  function addBooking() {
    const newBooking = { id: Date.now(), name: "Asha", room: 101 }
    console.log([...bookings, newBooking])
    setBookings([...bookings, newBooking])
  }

  function removeBooking(id) {
    setBookings(bookings.filter((b) => b.id !== id))
  }

  return (
    <div>
      <button onClick={addBooking}>Add booking</button>
      <ul>
        {bookings.map((b) => (
          <li key={b.id}>
            {b.name} - Room {b.room}
            <button onClick={() => removeBooking(b.id)}>Cancel</button>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default BookingList