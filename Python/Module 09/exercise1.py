class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

car = Car("ABC-123", 142)

print(f"License plate: {car.license_plate}")
print(f"Maximum speed: {car.maximum_speed} km/h")
print(f"Current speed: {car.current_speed} km/h")
print(f"Travelled distance: {car.travelled_distance} km")

"""
Note for myself:

1) Add class Name:
2) Add within the class a function called def __init__():. This means: When a class is called, run this function.
3) Always the first parameter must be self to initialize the object. Self means the particular object we are working with, aka the specific object I'm creating. In this case, the specific car I'm creating (car =).

4) Add the other parameters (the ones that are soft-coded) to the function (): def __init__ (self, parameter1, parameter2):
The teacher explained that we could add the values that are mandatory 0 within the parenthesis or within the body of the function.
The difference is:

 - Within the parenthesis: That way the values will be set as default for when the function is called and no arguments are passed.
 - Within the function body: We add there values that we will never need them coming from "outside", so we will never need those values to be passed when calling the function.

5) Inside of the function, add self.parameter (property) for each characteristic you want your class to have.
If it happens that one of those characteristics must be whatever parameter to entered, equal it to it.
Ex:
    self.license_plate = license_plate     # Here license_plate is coming from the parameters coming above and self.license_plate could be called whatever we want self.whatever_name
    self.maximum_speed = maximum_speed
Then, you can add "independent" ones as the fixed values.
Ex:
    self.current_speed = 0
    self.travelled_distance = 0

6) If you will want to use these values to print something, create a variable (car) and equal it to the class call with the corresponding parameters inside.
car = Car("ABC-123", 142)

7) Now you can print whatever you need referencing the car variable:
print(f"License plate: {car.license_plate}")                     # Note: The reference .license_plate refers to the name you gave to the self.
print(f"Maximum speed: {car.maximum_speed} km/h")
print(f"Current speed: {car.current_speed} km/h")
print(f"Travelled distance: {car.travelled_distance} km")
"""