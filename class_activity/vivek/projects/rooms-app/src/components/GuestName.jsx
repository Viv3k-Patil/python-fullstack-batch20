import { useState } from "react"
function GuestName() {
  const [name, setName] = useState("")
  console.log(`${name}, component isrendered`)

  return (
    <div>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Guest name"
      />
      <p>Hello, {name || "guest"}! 👋</p>
    </div>
  )
}

export default GuestName