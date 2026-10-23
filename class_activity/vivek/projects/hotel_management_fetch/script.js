// ----- Data -----
const rooms = [
  { no: 101, type: "Standard", price: 3000 },
  { no: 102, type: "Standard", price: 3000 },
  { no: 201, type: "Deluxe", price: 4500 },
  { no: 202, type: "Deluxe", price: 4500 },
  { no: 301, type: "Suite", price: 7000 },
  { no: 302, type: "Suite", price: 7000 }
];

// Load saved bookings when the page opens
let bookings = JSON.parse(localStorage.getItem("bookings")) || [];

// ----- Elements -----
const roomsDiv = document.getElementById("rooms");
const form = document.getElementById("bookingForm");
const guestName = document.getElementById("guestName");
const roomSelect = document.getElementById("roomSelect");
const checkIn = document.getElementById("checkIn");
const checkOut = document.getElementById("checkOut");
const msg = document.getElementById("msg");
const filterName = document.getElementById("filterName");
const filterType = document.getElementById("filterType");
const tbody = document.getElementById("tbody");

// ----- Helpers -----
function save() {
  localStorage.setItem("bookings", JSON.stringify(bookings));
}

function isBooked(roomNo) {
  return bookings.some((b) => b.roomNo === roomNo);
}

// ----- Render: rooms dashboard -----
function renderRooms() {
  roomsDiv.innerHTML = "";
  rooms.forEach((r) => {
    const booked = isBooked(r.no);
    const card = document.createElement("div");
    card.className = "card " + (booked ? "booked" : "free");
    card.innerText = `Room ${r.no} | ${r.type} | ₹${r.price} | ${booked ? "Booked" : "Available"}`;
    roomsDiv.appendChild(card);
  });
}

// ----- Render: room dropdown (available rooms only) -----
function renderRoomSelect() {
  roomSelect.innerHTML = '<option value="">Select room</option>';
  rooms.filter((r) => !isBooked(r.no)).forEach((r) => {
    const opt = document.createElement("option");
    opt.value = r.no;
    opt.innerText = `${r.no} - ${r.type} (₹${r.price})`;
    roomSelect.appendChild(opt);
  });
}

// ----- Render: bookings table (with filters) -----
function renderBookings() {
  const nameText = filterName.value.trim().toLowerCase();
  const typeText = filterType.value;
  tbody.innerHTML = "";

  bookings
    .filter((b) => b.name.toLowerCase().includes(nameText))
    .filter((b) => typeText === "" || b.type === typeText)
    .forEach((b) => {
      const tr = document.createElement("tr");
      [b.name, b.roomNo, b.type, b.checkIn, b.checkOut, b.nights, "₹" + b.total].forEach((text) => {
        const td = document.createElement("td");
        td.innerText = text;
        tr.appendChild(td);
      });

      const td = document.createElement("td");
      const btn = document.createElement("button");
      btn.innerText = "Delete";
      btn.addEventListener("click", () => {
        bookings = bookings.filter((x) => x.id !== b.id);
        save();
        refresh();
      });
      td.appendChild(btn);
      tr.appendChild(td);
      tbody.appendChild(tr);
    });
}

function refresh() {
  renderRooms();
  renderRoomSelect();
  renderBookings();
}

// ----- Booking form -----
form.addEventListener("submit", (e) => {
  e.preventDefault();

  const name = guestName.value.trim();
  const roomNo = Number(roomSelect.value);
  let error = "";

  if (name.length < 3) error = "Name must be at least 3 characters.";
  else if (!roomNo) error = "Please select a room.";
  else if (!checkIn.value || !checkOut.value) error = "Please choose both dates.";
  else if (checkOut.value <= checkIn.value) error = "Check-out must be after check-in.";

  if (error) {
    msg.innerText = error;
    msg.className = "error";
    return;
  }

  const room = rooms.find((r) => r.no === roomNo);
  const nights = Math.round((new Date(checkOut.value) - new Date(checkIn.value)) / 86400000);

  bookings.push({
    id: Date.now(),
    name,
    roomNo,
    type: room.type,
    checkIn: checkIn.value,
    checkOut: checkOut.value,
    nights,
    total: nights * room.price
  });

  save();
  form.reset();
  msg.innerText = "Booking saved ✅";
  msg.className = "ok";
  refresh();
});

// ----- Filters -----
filterName.addEventListener("input", renderBookings);
filterType.addEventListener("change", renderBookings);

// ----- Start: load and render on page load -----
refresh();