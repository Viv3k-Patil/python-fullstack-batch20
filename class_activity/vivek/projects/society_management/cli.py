"""
cli.py — interactive, menu-driven front-end for the society management app.

This file contains ONLY input/output and menu wiring. All real logic still
lives in services/ and models/ — the CLI just calls those, the same way
main.py does for the scripted demo.
"""

from datetime import date

from models import Society, Building, Flat, Resident, Vehicle, VehicleType
from repositories.society_repository import SocietyRepository
from services import parking_service, amenity_service, maintenance_service


repo = SocietyRepository()
current_society: Society | None = None


# ---------------------------------------------------------------------
# Small input helpers
# ---------------------------------------------------------------------

def ask(prompt: str) -> str:
    return input(prompt).strip()


def ask_float(prompt: str) -> float:
    while True:
        value = ask(prompt)
        try:
            return float(value)
        except ValueError:
            print("❌ Please enter a valid number.")


def ask_int(prompt: str) -> int:
    while True:
        value = ask(prompt)
        try:
            return int(value)
        except ValueError:
            print("❌ Please enter a valid whole number.")


def ask_yes_no(prompt: str) -> bool:
    return ask(prompt + " (y/n): ").lower().startswith("y")


def require_society() -> bool:
    if current_society is None:
        print("❌ No society selected yet. Create or select one first (Main Menu option 1 or 2).")
        return False
    return True


def pick_building(society: Society) -> Building | None:
    if not society.buildings:
        print("❌ No buildings yet. Add one first.")
        return None
    print("Buildings:", ", ".join(society.buildings.keys()))
    name = ask("Enter building name: ")
    if name not in society.buildings:
        print("❌ Building not found.")
        return None
    return society.buildings[name]


def pick_flat(building: Building) -> Flat | None:
    if not building.flats:
        print("❌ No flats in this building yet.")
        return None
    print("Flats:", ", ".join(building.flats.keys()))
    flat_no = ask("Enter flat number: ")
    if flat_no not in building.flats:
        print("❌ Flat not found.")
        return None
    return building.flats[flat_no]


# ---------------------------------------------------------------------
# Menu actions
# ---------------------------------------------------------------------

def create_society():
    global current_society
    name = ask("Society name: ")
    if repo.exists(name):
        print("❌ A society with that name already exists.")
        return
    total_spots = ask_int("Total parking spots: ")
    current_society = Society(name, total_parking_spots=total_spots)
    repo.add(current_society)
    print(f"✅ Society '{name}' created and selected.")


def select_society():
    global current_society
    societies = repo.list_all()
    if not societies:
        print("❌ No societies exist yet. Create one first.")
        return
    print("Available societies:", ", ".join(s.name for s in societies))
    name = ask("Enter society name to select: ")
    if not repo.exists(name):
        print("❌ Society not found.")
        return
    current_society = repo.get(name)
    print(f"✅ Now working with society '{name}'.")


def add_building():
    if not require_society():
        return
    name = ask("Building name: ")
    if name in current_society.buildings:
        print("❌ A building with that name already exists.")
        return
    current_society.add_building(Building(name))
    print(f"✅ Building '{name}' added.")


def add_flat():
    if not require_society():
        return
    building = pick_building(current_society)
    if building is None:
        return
    flat_no = ask("Flat number (e.g. A-101): ")
    if flat_no in building.flats:
        print("❌ A flat with that number already exists.")
        return
    size = ask_float("Flat size (sqft): ")
    building.add_flat(Flat(flat_no, size))
    print(f"✅ Flat '{flat_no}' added to '{building.name}'.")


def add_resident():
    if not require_society():
        return
    building = pick_building(current_society)
    if building is None:
        return
    flat = pick_flat(building)
    if flat is None:
        return
    name = ask("Resident name: ")
    phone = ask("Resident phone: ")
    flat.add_resident(Resident(name, phone))
    print(f"✅ Resident '{name}' added to flat '{flat.flat_no}'.")


def add_vehicle():
    if not require_society():
        return
    building = pick_building(current_society)
    if building is None:
        return
    flat = pick_flat(building)
    if flat is None:
        return
    plate = ask("Vehicle number plate: ")
    print("Vehicle types: 1) Two-wheeler  2) Four-wheeler")
    choice = ask("Choose type: ")
    vtype = VehicleType.TWO_WHEELER if choice == "1" else VehicleType.FOUR_WHEELER
    flat.add_vehicle(Vehicle(plate, vtype))
    print(f"✅ Vehicle '{plate}' added to flat '{flat.flat_no}'.")


def assign_parking():
    if not require_society():
        return
    building = pick_building(current_society)
    if building is None:
        return
    flat = pick_flat(building)
    if flat is None:
        return
    if flat.has_parking:
        print("❌ This flat already has a parking spot assigned.")
        return
    success = parking_service.assign_parking(current_society, flat)
    if success:
        print(f"✅ Parking spot assigned to '{flat.flat_no}'.")
    else:
        print("❌ No parking spots available.")
    print(f"Spots left: {parking_service.available_spots(current_society)}")


def generate_bills():
    if not require_society():
        return
    month = ask("Month to bill (e.g. 2026-08): ")
    rate = ask_float("Rate per sqft (default 3): ") or 3
    maintenance_service.generate_monthly_bills(current_society, month, rate)
    print(f"✅ Bills generated for {month} across all flats.")


def pay_bill():
    if not require_society():
        return
    building = pick_building(current_society)
    if building is None:
        return
    flat = pick_flat(building)
    if flat is None:
        return
    if not flat.bills:
        print("❌ This flat has no bills yet. Generate bills first.")
        return
    print("Months billed:", ", ".join(flat.bills.keys()))
    month = ask("Which month's bill to pay? ")
    if month not in flat.bills:
        print("❌ No bill for that month.")
        return
    bill = flat.bills[month]
    print(f"Due: ₹{bill.amount_due}, Already paid: ₹{bill.amount_paid}")
    amount = ask_float("Payment amount: ")
    maintenance_service.pay_bill(bill, amount)
    print(f"✅ Payment recorded. Fully paid: {bill.is_paid}")


def add_amenity():
    if not require_society():
        return
    name = ask("Amenity name (e.g. Gym, Clubhouse Hall): ")
    if name in current_society.amenities:
        print("❌ That amenity already exists.")
        return
    allow_multiple = ask_yes_no("Allow multiple bookings on the same day?")
    amenity_service.add_amenity(current_society, name, allow_multiple)
    print(f"✅ Amenity '{name}' added.")


def book_amenity():
    if not require_society():
        return
    names = amenity_service.list_amenities(current_society)
    if not names:
        print("❌ No amenities set up yet.")
        return
    print("Amenities:", ", ".join(names))
    name = ask("Amenity to book: ")
    if name not in current_society.amenities:
        print("❌ Amenity not found.")
        return
    date_str = ask("Booking date (YYYY-MM-DD): ")
    try:
        day = date.fromisoformat(date_str)
    except ValueError:
        print("❌ Invalid date format.")
        return
    success = amenity_service.book_amenity(current_society, name, day)
    print("✅ Booked!" if success else "❌ Slot already taken for that date.")


def raise_complaint():
    if not require_society():
        return
    building = pick_building(current_society)
    if building is None:
        return
    flat = pick_flat(building)
    if flat is None:
        return
    description = ask("Describe the issue: ")
    request = maintenance_service.raise_request(current_society, flat.flat_no, description)
    print(f"✅ Complaint raised for '{flat.flat_no}' (status: {request.status}).")


def resolve_complaint():
    if not require_society():
        return
    open_requests = [r for r in current_society.requests if r.status == "OPEN"]
    if not open_requests:
        print("❌ No open complaints.")
        return
    for i, r in enumerate(open_requests, start=1):
        print(f"{i}. Flat {r.flat_no}: {r.description}")
    index = ask_int("Pick a complaint number to resolve: ") - 1
    if index < 0 or index >= len(open_requests):
        print("❌ Invalid choice.")
        return
    request = open_requests[index]

    print("Worker type: 1) Plumber  2) Electrician")
    choice = ask("Choose type: ")
    worker_name = ask("Worker's name: ")
    worker = maintenance_service.Plumber(worker_name) if choice == "1" else maintenance_service.Electrician(worker_name)

    maintenance_service.resolve_request(request, worker)
    print(f"✅ Resolved: {request.resolution_note}")


def view_summary():
    if not require_society():
        return
    society = current_society
    print(f"\n📋 Society: {society.name}")
    print(f"Parking: {society.occupied_parking_spots}/{society.total_parking_spots} occupied")
    print(f"Amenities: {', '.join(society.amenities.keys()) or 'none'}")

    for building in society.buildings.values():
        print(f"\n🏢 {building.name}")
        for flat in building.flats.values():
            residents = ", ".join(r.name for r in flat.residents) or "none"
            bill_status = ", ".join(
                f"{m}:{'paid' if b.is_paid else 'unpaid'}" for m, b in flat.bills.items()
            ) or "no bills"
            print(f"   {flat.flat_no} | residents: {residents} | parking: {flat.has_parking} | bills: {bill_status}")

    open_count = sum(1 for r in society.requests if r.status == "OPEN")
    print(f"\n🛠️  Complaints: {len(society.requests)} total, {open_count} open")


# ---------------------------------------------------------------------
# Main menu loop
# ---------------------------------------------------------------------

MENU = """
========== 🏘️  SOCIETY MANAGEMENT SYSTEM ==========
 1. Create society
 2. Select society
 3. Add building
 4. Add flat
 5. Add resident
 6. Add vehicle
 7. Assign parking
 8. Generate monthly bills
 9. Pay a bill
10. Add amenity
11. Book amenity
12. Raise complaint
13. Resolve complaint
14. View society summary
 0. Exit
====================================================
"""

ACTIONS = {
    "1": create_society,
    "2": select_society,
    "3": add_building,
    "4": add_flat,
    "5": add_resident,
    "6": add_vehicle,
    "7": assign_parking,
    "8": generate_bills,
    "9": pay_bill,
    "10": add_amenity,
    "11": book_amenity,
    "12": raise_complaint,
    "13": resolve_complaint,
    "14": view_summary,
}


def main():
    print("Welcome! Start by creating a society (option 1).")
    while True:
        label = f" (current: {current_society.name})" if current_society else " (no society selected)"
        print(MENU.rstrip() + label)
        choice = ask("Enter choice: ")

        if choice == "0":
            print("Goodbye! 👋")
            break

        action = ACTIONS.get(choice)
        if action is None:
            print("❌ Invalid choice, try again.")
            continue

        try:
            action()
        except Exception as e:
            print(f"❌ Something went wrong: {e}")


if __name__ == "__main__":
    main()
