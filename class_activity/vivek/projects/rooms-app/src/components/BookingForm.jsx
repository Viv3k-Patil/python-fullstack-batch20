import { useState } from "react"

function BookingForm({ onBook }) {
  const [form, setForm] = useState({ 
    name: "", 
    roomType: "", 
    nights: 1, 
    agree: false 
})

  const [error, setError] = useState("")

  function handleChange(e) {
    const { name, value, type, checked } = e.target
    setForm({ ...form, [name]: type === "checkbox" ? checked : value })
  }

  function handleSubmit(e) {
    e.preventDefault()

    let message = ""
    if (form.name.trim().length < 3) message = "Name must be at least 3 characters."
    else if (!form.roomType) message = "Please choose a room type."
    else if (Number(form.nights) < 1) message = "Nights must be at least 1."
    else if (!form.agree) message = "Please accept the terms."

    if (message) {
      setError(message)
      return
    }

    setError("")
    onBook({
      id: Date.now(),
      name: form.name.trim(),
      roomType: form.roomType,
      nights: Number(form.nights),
    })
    setForm(emptyForm)        // clear the form
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        name="name"
        value={form.name}
        onChange={handleChange}
        placeholder="Guest name"
      />

      <select name="roomType" value={form.roomType} onChange={handleChange}>
        <option value="">Select room type</option>
        <option value="Standard">Standard</option>
        <option value="Deluxe">Deluxe</option>
        <option value="Suite">Suite</option>
      </select>

      <input
        type="number"
        name="nights"
        min="1"
        value={form.nights}
        onChange={handleChange}
      />

      <label>
        <input
          type="checkbox"
          name="agree"
          checked={form.agree}
          onChange={handleChange}
        />
        I accept the terms
      </label>

      <button type="submit">Book</button>

      {error && <p style={{ color: "red" }}>{error}</p>}
    </form>
  )
}

export default BookingForm