from datetime import date

from models import Society, Building, Flat, Resident
from repositories.society_repository import SocietyRepository
from services import parking_service, amenity_service, maintenance_service


def build_society(repo: SocietyRepository) -> Society:
    society = Society("Green Valley", total_parking_spots=5)

    tower_a = Building("Tower A")
    flat_101 = Flat("A-101", size_sqft=900)
    flat_101.add_resident(Resident("Priya Sharma", "9876543210"))
    tower_a.add_flat(flat_101)
    society.add_building(tower_a)

    amenity_service.add_amenity(society, "Gym", allow_multiple=True)
    amenity_service.add_amenity(society, "Clubhouse Hall", allow_multiple=False)

    repo.add(society)
    return society


def main():
    repo = SocietyRepository()
    build_society(repo)
    society = repo.get("Green Valley")
    flat_101 = society.buildings["Tower A"].get_flat("A-101")

    # --- Workflow 1: Parking ---
    print("Parking assigned:", parking_service.assign_parking(society, flat_101))
    print("Spots left:", parking_service.available_spots(society))

    # --- Workflow 2: Monthly billing ---
    maintenance_service.generate_monthly_bills(society, "2026-08")
    bill = flat_101.bills["2026-08"]
    print(f"A-101 bill: ₹{bill.amount_due}, paid={bill.is_paid}")
    maintenance_service.pay_bill(bill, 2700)
    print(f"After payment, paid={bill.is_paid}")

    # --- Workflow 3: Amenity booking ---
    print("Gym booking (always allowed):",
          amenity_service.book_amenity(society, "Gym", date.today()))
    print("Clubhouse booking 1:",
          amenity_service.book_amenity(society, "Clubhouse Hall", date(2026, 9, 1)))
    print("Clubhouse booking 2, same day (should fail):",
          amenity_service.book_amenity(society, "Clubhouse Hall", date(2026, 9, 1)))

    # --- Workflow 4: Complaint resolution (polymorphism in action) ---
    request = maintenance_service.raise_request(society, "A-101", "Leaking tap in kitchen")
    maintenance_service.resolve_request(request, maintenance_service.Plumber("Ramesh"))
    print(request.status, "-", request.resolution_note)


if __name__ == "__main__":
    main()
