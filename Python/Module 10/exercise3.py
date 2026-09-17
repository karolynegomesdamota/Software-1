class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, destination):
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

    def floor_down(self):
        self.current_floor = self.current_floor - 1

class Building:
    def __init__(self, bottom_floor, top_floor, amount_created_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(amount_created_elevators):
            i = Elevator(self.bottom_floor, self.top_floor)
            self.elevators.append(i)

    def run_elevator(self, number_of_elevator, destination):
        print(f"\nI'm currently running the elevator number {number_of_elevator}!")
        self.elevators[number_of_elevator].go_to_floor(destination)

    def fire_alarm(self):
        for i in range(len(self.elevators)):
            print("\nFire! Sending all elevators down...")
            self.run_elevator(i, self.bottom_floor)

building = Building(1, 10, 3)

building.run_elevator(0, 3) # Sending all elevators to the third floor to try the fire alarm.
building.run_elevator(1, 3) # Sending all elevators to the third floor to try the fire alarm.
building.run_elevator(2, 3) # Sending all elevators to the third floor to try the fire alarm.

building.fire_alarm()

print("\nTesting elevators going up again to check if they have been sent to the bottom floor: ")

building.run_elevator(0, 5)
building.run_elevator(1, 5)
building.run_elevator(2, 5)