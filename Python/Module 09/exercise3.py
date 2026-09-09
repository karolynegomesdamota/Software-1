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
        self.travelled_distance = number_of_hours * self.current_speed

car = Car("ABC-123", 142)
print(f"Initial distance: {car.travelled_distance} km")
car.current_speed = 60
car.drive(1.5)
print(f"Distance after driving 1.5 hours at 60 km/h: {car.travelled_distance} km")


# This is working but Moodle does not accept the code!!!