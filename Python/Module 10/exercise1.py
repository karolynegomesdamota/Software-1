class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, destination):
        self.destination = destination
        if self.current_floor < self.destination and self.destination <= self.top_floor:
            self.floor_up()
        elif self.current_floor > self.destination and self.destination >= self.bottom_floor:
            self.floor_down()
        else:
            print(f"The floor {destination} does not exist!")

    def floor_up(self):
        self.current_floor = self.current_floor + (self.destination - self.current_floor)
        print(f"The current floor is {self.current_floor}")

    def floor_down(self):
        self.current_floor = self.current_floor - (self.current_floor - self.destination)
        print(f"The current floor is {self.current_floor}")

h = Elevator(1, 10)
print("Basic elevator test:")
h.go_to_floor(5)
h.go_to_floor(1)

# Code working correctly, but Moodle does not accept it.