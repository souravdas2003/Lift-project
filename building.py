class Building:
    def __init__(self, num_floors, lifts):
        self.num_floors = num_floors
        self.lifts = lifts

    def process_request(self, request):
        starting_floor, destination_floor = request
        for lift in self.lifts:
            if lift.current_floor == starting_floor:
                lift.move_to_floor(destination_floor)
                return
        # If no suitable lift found on the starting floor, find the closest lift
        closest_lift = min(self.lifts, key=lambda x: abs(x.current_floor - starting_floor))
        closest_lift.move_to_floor(starting_floor)
        closest_lift.move_to_floor(destination_floor)
