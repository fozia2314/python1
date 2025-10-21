import random


class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        new_speed = self.current_speed + change_of_speed
        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


def race():
    cars = []
    for i in range(1, 11):
        license_plate = f"ABC-{i}"
        maximum_speed = random.randint(100, 200)
        car = Car(license_plate, maximum_speed)
        cars.append(car)
    race_over = False
    while not race_over:
        for car in cars:
            change_of_speed = random.randint(-10, 15)
            car.accelerate(change_of_speed)
            car.drive(1)
            if car.travelled_distance >= 10000:
                race_over = True

    return sorted(cars, key=lambda c: c.travelled_distance, reverse=True)