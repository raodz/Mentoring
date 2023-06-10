class Vehicle:
    def __init__(self, max_velocity_: float, course_: float):
        self.max_velocity = max_velocity_
        self.course = course_

    def increase_course(self, distance: float):
        self.course += distance


def main():
    some_vehicle = Vehicle(123.0, 134.5)
    print(some_vehicle.course)
    some_vehicle.increase_course(21.5)
    print(some_vehicle.course)


if __name__ == '__main__':
    main()
