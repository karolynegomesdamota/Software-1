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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            print(car.license_plate)
            car.accelerate(random.randint (-10, 15))
            print(car.current_speed)
            car.drive(1)
            print(car.travelled_distance)

    def print_status(self):
        for car in self.cars:
            print(f"Car license plate: {car.license_plate}")
            print(f"Car maximum speed: {car.maximum_speed}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
            else:
                return False

#Code from Moodle to test this:

cars = []
for i in range(10):
    car = Car(f"ABC-{i+1}", random.randint(100, 200))
    cars.append(car)

race = Race("Grand Demolition Derby", 8000, cars)
print(f"Race created: {race.name} ({race.distance} km)")
print(f"Cars participating: {len(race.cars)}")

print(f"\nRace finished initially: {race.race_finished()}")

for hour in range(5):
    race.hour_passes()
    if hour == 2:
        print(f"After {hour+1} hours, race finished: {race.race_finished()}")