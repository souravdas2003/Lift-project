class Lift:
    def __init__(self):
        self.current_floor = 0
        self.state = "CLOSE"

    def move_to_floor(self, floor):
        if floor > self.current_floor:
            self.state = "OPEN"
            self.current_floor = floor
            self.state = "CLOSE"
        elif floor < self.current_floor:
            self.state = "OPEN"
            self.current_floor = floor
            self.state = "CLOSE"

class Building:
    def __init__(self, num_floors, lifts):
        self.num_floors = num_floors
        self.lifts = lifts

    def process_request(self, request):
        for lift in self.lifts:
            if lift.state == "CLOSE":
                lift.move_to_floor(request[1])
                break

def run_test_cases():
    building = Building(num_floors=10, lifts=[Lift(), Lift()])

    test_cases = [
        ([0, 7]),
        ([3, 0])
    ]

    for i, test_case in enumerate(test_cases):
        print(f"T={i}")
        building.process_request(test_case)
        print(f"LIFT 1 -- > {building.lifts[0].current_floor} ({building.lifts[0].state}), LIFT 2 ---> {building.lifts[1].current_floor} ({building.lifts[1].state})")
        print()

run_test_cases()
