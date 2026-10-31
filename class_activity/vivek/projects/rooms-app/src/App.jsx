// // import Counter from './components/Notes'
// import BookingList from './components/Booking'
// import ShowHide from './components/ShowHide'
// import Component from './components/component'
// import BookButton from './components/Event'
// import GuestName from './components/GuestName'
// function App() {

//   return (
//     <>
//       {/* <Counter /> */}
//       {/* <Component />
//       <ShowHide />
//       <BookingList />
//       <BookButton />
//       <GuestName /> */}
//     </>
    
//   )
// }

// export default App


import { useState } from "react"
import BookingForm from "./components/BookingForm"

function App() {
  const [bookings, setBookings] = useState([])

  function addBooking(booking) {
    setBookings([...bookings, booking])
  }

  function removeBooking(id) {
    setBookings(bookings.filter((b) => b.id !== id))
  }

  return (
    <div>
      <h1>🏨 Hotel Paradise</h1>
      <BookingForm onBook={addBooking} />

      <h2>Bookings ({bookings.length})</h2>
      <ul>
        {bookings.map((b) => (
          <li key={b.id}>
            {b.name} - {b.roomType}, {b.nights} night(s)
            <button onClick={() => removeBooking(b.id)}>Cancel</button>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App