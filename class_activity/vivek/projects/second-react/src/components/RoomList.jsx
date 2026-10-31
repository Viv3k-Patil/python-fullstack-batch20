
function RoomList() {
    const rooms = [
        { id: 1, no: 101, type: "Standard", price: 3000 },
        { id: 2, no: 201, type: "Deluxe", price: 4500 },
        { id: 3, no: 301, type: "Suite", price: 7000 },
    ]

    

  return (
    <div>
        <ul>
            {
                rooms.map((room) =>
                    <li>
                        Room: {room.no} - Room-Type: {room.type} - Price$: {room.price}   
                    </li>
                )
            }
        </ul>
    </div>
  )
}

export default RoomList