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
        print(f"We have reached floor {self.current_floor}!")

    def floor_down(self):
        self.current_floor = self.current_floor - (self.current_floor - self.destination)
        print(f"We have reached floor {self.current_floor}!")

class Building:
    def __init__(self, bottom_floor, top_floor, amount_created_elevators):
        self.list_of_elevators = []
        for i in range(amount_created_elevators):
            i = Elevator(bottom_floor, top_floor)
            self.list_of_elevators.append(i)

    def run_elevator(self, number_of_elevator, destination):
        print(f"\nI'm currently running the elevator number {number_of_elevator}!")
        self.list_of_elevators[number_of_elevator-1].go_to_floor(destination)

    def fire_alarm(self):
        for i in range(len(self.list_of_elevators)):
            print("\nFire! Sending all elevators down...")
            self.run_elevator(i+1, 1)

building = Building(1, 10, 3)

building.run_elevator(1, 3) # Sending all elevators to the third floor to try the fire alarm.
building.run_elevator(2, 3) # Sending all elevators to the third floor to try the fire alarm.
building.run_elevator(3, 3) # Sending all elevators to the third floor to try the fire alarm.

building.fire_alarm()

print("\nTesting elevators going up again to check if they have been sent to the bottom floor: ")

building.run_elevator(1, 5)
building.run_elevator(2, 5)
building.run_elevator(3, 5)

# Code working correctly, but Moodle does not accept it.