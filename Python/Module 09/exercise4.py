import random

class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate (self, change_of_speed):
        if change_of_speed > 0:
            for _ in range(change_of_speed):
                if self.current_speed < self.maximum_speed:
                    self.current_speed = self.current_speed + 1
        elif change_of_speed < 0:
            for _ in range(-1 * change_of_speed):
                if self.current_speed > 0:
                    self.current_speed = self.current_speed - 1

    def drive(self, number_of_hours):
        self.travelled_distance = self.travelled_distance + (number_of_hours * self.current_speed)

# Main program:

def race(list):
    race_continues = True
    while race_continues:
        for car in list:
            car.accelerate(random.randint (-10, 15))
            car.drive(1)
            if car.travelled_distance >= 10000:
                race_continues = False
                break
    return list

list_of_cars = []

list_of_cars.append(Car("ABC-123", 100))
list_of_cars.append(Car("DEF-456", 120))
list_of_cars.append(Car("GHJ-789", 140))

results = race(list_of_cars)

"""
Note for myself: I was struggling to solve this one because I did not pay attention to the requirements.
It asked for a function and I added a method to the class.

# Explanation of function:

def race(list):                                                           # List here is just a placeholder to tell the program that when we call this function, it must have a parameter.
    race_continues = True                                                 # Added this in order to run the while.
    while race_continues:                                                 # While race_continues is True, it will continue looping.
        for car in list:                                                  # This to loop through all the cars of the list, one by one.
            car.accelerate(random.randint (-10, 15))                      # Calling the method to change the speed of the specific car by some number between -10 and 15.
            car.drive(1)                                                  # Calling this method to make each car run for 1 hour.
            print(f"The car {i.license_plate} speed now is {i.current_speed} and has driven this distance: {i.travelled_distance}.")      # This was added just to make the code more clear to myself. I had to remove this from the main code for Moodle to accept it.
             if car.travelled_distance >= 1000:                            # Added this to stop the race when any of the cars reaches 1000.
                race_continues = False
                break
    return list                                                            # This was added to return the list as the exercise requires.

"""