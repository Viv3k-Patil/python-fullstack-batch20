def dynamic_price_generator(base_price, total_seats):
    seats_sold = 0
    while seats_sold < total_seats:
        seats_sold += 1
        demand_ratio = seats_sold / total_seats          # how "full" the event is, from 0.0 to 1.0

        if demand_ratio < 0.5:
            price = base_price                               # low demand — base price
        elif demand_ratio < 0.8:
            price = base_price * 1.2                          # medium demand — 20% increase
        else:
            price = base_price * 1.5                           # high demand — 50% increase

        yield {
            "ticket_number": seats_sold,
            "price": round(price, 2),
            "demand_ratio": round(demand_ratio, 2)
        }

pricing = dynamic_price_generator(base_price=1000, total_seats=10)

for ticket in pricing:
    print(f"Ticket #{ticket['ticket_number']}: ₹{ticket['price']} (demand: {ticket['demand_ratio']*100:.0f}%)")