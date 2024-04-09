# main.py
from lift import Lift
from building import Building

def main():
    # Input parameters
    N = int(input("Enter the number of lifts: "))
    M = int(input("Enter the number of floors: "))
    lifts = [Lift() for _ in range(N)]  # Create N lifts

    # Lift requests
    requests = []
    while True:
        request = input("Enter lift request (format: starting_floor destination_floor), or 'done' to exit: ")
        if request == 'done':
            break
        requests.append(tuple(map(int, request.split())))

    # Building instance
    building = Building(M, lifts)

    # Process requests
    for request in requests:
        building.process_request(request)

if __name__ == "__main__":
    main()
