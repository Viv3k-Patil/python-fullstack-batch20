

def ticket_id_generator():
    ticket = 1
    while ticket <= 3000:
        yield f"TICKET-ID: {ticket}"
        ticket += 1

gen = ticket_id_generator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
