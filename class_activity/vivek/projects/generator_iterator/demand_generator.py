import random
import time

def live_demand_stream():
    while True:
        demand_level = random.choice(["low", "medium", "high", "No demand at all", "blocked"])
        yield demand_level
        time.sleep(1)          # simulates a new demand reading arriving every second

demand_gen = live_demand_stream()

for i in range(10):                     # only look at the first 5 "live updates" for this demo
    current_demand = next(demand_gen)
    print(f"📡 Live demand update: {current_demand}")