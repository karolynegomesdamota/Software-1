# COMPLEX VERSION OF THE CODE BUT EASIER TO UNDERSTAND ON TERMINAL:

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, destination):
        print(f"\nCurrent floor: {self.current_floor}. Destination: {destination}.")
        if self.current_floor < destination and destination <= self.top_floor:
            while self.current_floor != destination:
                self.floor_up()
            print(f"We have reached floor {self.current_floor}!")
        elif self.current_floor > destination and destination >= self.bottom_floor:
            while self.current_floor != destination:
                self.floor_down()
            print(f"We have reached floor {self.current_floor}!")
        else:
            print(f"The floor {destination} does not exist!")

    def floor_up(self):
        self.current_floor = self.current_floor + 1
        print(f"Going up... {self.current_floor}")

    def floor_down(self):
        self.current_floor = self.current_floor - 1
        print(f"Going down... {self.current_floor}")

h = Elevator(1, 10)
print("\nBasic elevator test:")
h.go_to_floor(5)
h.go_to_floor(1)

# Modifications done to match the simple version logic.
# Now I make the elevator move one by one when it goes up and down. And within the method go_to_floor, I loop it over and over until we reach the destination.