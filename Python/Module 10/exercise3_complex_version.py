# COMPLEX VERSION OF THE CODE BUT EASIER TO UNDERSTAND ON TERMINAL:

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
        print(f"\nCurrent floor: {self.current_floor}. Destination: {self.destination}.")
        while self.current_floor < self.destination:
            self.current_floor += 1
            print(f"Going up... {self.current_floor}")
        self.current_floor = self.current_floor + (self.destination - self.current_floor) # We add to the current floor the difference between the current floor and the destination.
        print(f"We have reached floor {self.current_floor}!")

    def floor_down(self):
        print(f"\nCurrent floor: {self.current_floor}. Destination: {self.destination}.")
        while self.current_floor > self.destination:
            self.current_floor -= 1
            print(f"Going down... {self.current_floor}")
        self.current_floor = self.current_floor - (self.current_floor - self.destination) # We subtract to the current floor the difference between the current floor and the destination.
        print(f"We have reached floor {self.current_floor}!")

class Building:
    def __init__(self, bottom_floor, top_floor, amount_created_elevators):
        self.list_of_elevators = [] # This is out because inside the for/in, it was not adding up the number.
        for i in range(amount_created_elevators): # This to create a new elevator per each individual elevator within the amount the user/method-calling wants to create.
            i = Elevator(bottom_floor, top_floor)
            self.list_of_elevators.append(i) # This to the new elevator to the list.

    def run_elevator(self, number_of_elevator, destination): # Number of elevator here has no connection to the amount created. You are actually selecting one specific elevator from those created.
        print(f"\nI'm currently running the elevator number {number_of_elevator}!")
        self.list_of_elevators[number_of_elevator-1].go_to_floor(destination) # [number_of_elevator-1] to access the correct index within the list since the user/method-calling will not be considering the existence of an elevator number 0.
                                                                              # .go_to_floor applies only to that specific elevator we select and pass the destination to it, which is the floor the user/method-calling wants to go to.

    def fire_alarm(self):
        for i in range(len(self.list_of_elevators)):
            print("\nFire! Sending all elevators down...")
            self.run_elevator(i+1, 1) # i+1 to correctly set the number_of_elevator since later within the run_elevator method it will run [number_of_elevator-1].

building = Building(1, 10, 3)

building.run_elevator(1, 3) # Sending all elevators to the third floor to try the fire alarm.
building.run_elevator(2, 3) # Sending all elevators to the third floor to try the fire alarm.
building.run_elevator(3, 3) # Sending all elevators to the third floor to try the fire alarm.

building.fire_alarm()

print("\nTesting elevators going up again to check if they have been sent to the bottom floor: ")

building.run_elevator(1, 5)
building.run_elevator(2, 5)
building.run_elevator(3, 5)
