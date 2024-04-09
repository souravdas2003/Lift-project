class Lift:
    def __init__(self):
        self.current_floor = 0
        self.state = "CLOSE"  # Initial state: closed

    def move_to_floor(self, destination_floor):
        # Simulate moving to the destination floor
        self.state = "OPEN"
        print(f"LIFT -- > {destination_floor} (OPEN)")
        self.state = "CLOSE"
        print(f"LIFT -- > {destination_floor} (CLOSE)")

