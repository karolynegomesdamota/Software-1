class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate (self, change_of_speed):
        self.change_of_speed = change_of_speed              # Just found out this can be removed and it works. Find out why.
        if change_of_speed > 0:
            for _ in range(change_of_speed):
                if self.current_speed < self.maximum_speed:
                    self.current_speed = self.current_speed + 1
        elif change_of_speed < 0:
            for _ in range(-1 * change_of_speed):
                if self.current_speed > 0:
                    self.current_speed = self.current_speed - 1

car = Car("ABC-123", 142)
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"Current speed: {car.current_speed} km/h")
car.accelerate(-200)
print(f"Current speed: {car.current_speed} km/h")

"""
Note for myself:

Above is the code accepted by Moodle. Below the code with some print additions to make it more clear.

class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

        print (f"The previous speed was {self.current_speed} ")


    def accelerate (self, change_of_speed):                                 # New function added with the requested name and receiving the requested parameters
        self.change_of_speed = change_of_speed                              # This is done to assign a value to the self.change_of_speed.
        if change_of_speed > 0:                                             # From here, we are referencing the parameter we passed. So, why is the self one necessary? Ask teacher.
            for _ in range(change_of_speed):                                # Loop for the amount of times set by the change of speed.
                if self.current_speed < self.maximum_speed:                 # Using the current_speed from the init function, we check if it is less than the limit.
                    self.current_speed = self.current_speed + 1             # If the previous condition was met, then we add +1 to the speed. This will happen many times according to the loop mentioned before.
                    print (f"The speed is now {self.current_speed} ")
        elif change_of_speed < 0:                                           # Same logic than above, but opposite.
            for _ in range(-1 * change_of_speed):                           # Loop for the amount of times set by the change of speed.
                if self.current_speed > 0:                                  # Using the current_speed from the init function, we check if it is more than 0.
                    self.current_speed = self.current_speed - 1             # If the previous condition was met, then we reduce -1 to the speed. This will happen many times according to the loop mentioned before.
                    print (f"The speed is now {self.current_speed} ")
"""