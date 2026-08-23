
# data model
rooms = {
        101: "Available", 
        102: "Available", 
        103: "Available", 
        104: "Available"
    }
bookings = {}   # will store: {room_number: {"name": ..., "phone": ..., "days": ...}}

# helper functions
def view_available_rooms():
    for room_number, status in rooms.items():
        if status == "Available":
            print(f"✅ {room_number} : Available")

def book_room():
    view_available_rooms()
    room_number = int(input("Enter room number you want book?: "))


    # name, phone number, days
    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    days = input("days of stay: ")

    rooms[room_number] = "Booked"
    bookings[room_number] = {"name": name, "phone": phone_number, "days": days}

    print(f"✅ Room {room_number} successfully booked for {name} ({days} days)!")


def cancel_booking():
    room_number = int(input("Enter room number to cancel: "))

    del bookings[room_number]
    rooms[room_number] = "Available"
    print(f"✅ Booking in Room {room_number} has been cancelled.")


def view_all_bookings():
    for room_number, details in bookings.items():
        print(f"Room {room_number}: {details['name']} | {details['phone']} | {details['days']} days")

def search_booking():
    keyword = input("Enter customer name or room number to search: ")

    for room_number, details in bookings.items():
        if keyword == details["name"] or keyword == str(room_number):
            print(f"🔍 Found: Room {room_number} — {details['name']}, {details['phone']}, {details['days']} days")

# admin options
while True:
    print("""
        ===== 🏨 HOTEL MANAGEMENT SYSTEM =====
        1. View Available Rooms
        2. Book a Room
        3. Cancel a Booking
        4. View All Bookings
        5. Search Booking
        6. Exit
        =======================================
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        view_available_rooms()
    elif choice == 2:
        book_room()
    elif choice == 3:
        cancel_booking()
    elif choice == 4:
        view_all_bookings()
    elif choice == 5:
        search_booking()
    elif choice == 6:
        print("Thank you for using Hotel Management System! 👋")
        break
    else:
        print("Invalid choice, please try again.")
