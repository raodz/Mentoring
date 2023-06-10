class Depot:
    def __init__(self, name: str, kind: str, vehicles: list):
        self.name = name
        self.kind = kind
        self.vehicles = vehicles

    def __str__(self):
        return f'This is the {self.name} depot. It is a {self.kind} depot including' \
               f' vehicles: {self.vehicles}'

class Vehicle:
    def __init__(self, number: int, kind: str, depot: Depot, max_velocity: float):
        self.number = number
        self.depot = depot
        self.max_velocity = max_velocity
        self.kind = kind

    def __str__(self):
        return f'This is the {self.kind} nr. {self.number} of the {self.depot.name} ' \
               f'depot. ' \
               f'Its maximal velocity is {self.max_velocity} km/h.'

class Tram(Vehicle):
    def __init__(self, number, depot, max_velocity, cars_number: int):
        super().__init__(number, 'tram', depot, max_velocity)
        self.cars_number = cars_number

    def __str__(self):
        return super().__str__() + f' It has {self.cars_number} cars.'

class Bus(Vehicle):
    def __init__(self, number, depot, max_velocity, used_fuel: float):
        super().__init__(number, 'bus', depot, max_velocity)
        self.used_fuel = used_fuel

    def __str__(self):
        return super().__str__() + f' This month it has already ' \
                                   f'used {self.used_fuel} liters of fuel.'

def main():
    some_vehicle = Vehicle(4, 'tram', Depot('WOLA', 'tram', []), 80)
    print(some_vehicle)
    some_tram = Tram(24, Depot('WOLA', 'tram', []), 90, 3)
    print(some_tram)
    some_bus = Bus(123, Depot('OSTROBRAMSKA', 'bus', []), 120, 23.4)
    print(some_bus)

if __name__ == '__main__':
    main()
