class Elevator:
    def __init__(self, min_floor, max_floor):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.floor = min_floor

    def go_to_floor(self, number_floor):
        self.number_floor = number_floor                                                             #Is this the correct way of doing this? I had to add this here, in order for it to work.
        if self.floor < self.number_floor and self.number_floor <= self.max_floor:
            self.floor_up()
        elif self.floor > self.number_floor and self.number_floor >= self.min_floor:
            self.floor_down()
        else:
            print(f"The floor {number_floor} does not exist!")

    def floor_up(self):
        self.floor = self.floor + (self.number_floor - self.floor)
        print(f"The current floor is {self.floor}")
    def floor_down(self):
        self.floor = self.floor - (self.floor - self.number_floor)
        print(f"The current floor is {self.floor}")


h = Elevator(1, 10)
print("Basic elevator test:")
h.go_to_floor(5)
h.go_to_floor(1)

# Code working correctly, but Moodle does not accept it.