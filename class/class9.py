from datetime import datetime


class Operation:
    def __init__(self, name: str, time: datetime, water_amount: float, success: bool):
        self.name = name
        self.time = time
        self.water_amount = water_amount
        self.success = success


class Tank:
    def __init__(self, name: str, capacity: float, filling: float = 0,
                 history: list = []):
        self.name = name
        self.capacity = capacity
        self.filling = filling
        self.history = history

    def __str__(self):
        return self.name

    def pour_water(self, volume: float):
        if self.filling + volume <= self.capacity:
            self.filling += volume
            current_operation = Operation('pour_water', datetime.now(), volume, True)
            self.history.append(current_operation)
        else:
            print('This amount of water will not fit in the tank')
            current_operation = Operation('pour_water', datetime.now(), volume, False)
            self.history.append(current_operation)

    def pour_out_water(self, volume: float):
        if self.filling - volume >= 0:
            self.filling -= volume
            current_operation = Operation('pour_out_water', datetime.now(), volume,
                                          True)
            self.history.append(current_operation)
        else:
            print('There is not as much water in the tank')
            current_operation = Operation('pour_out_water', datetime.now(), volume,
                                          False)
            self.history.append(current_operation)

    def transfer_water(self, from_tank, volume: float):
        if volume <= (self.capacity - self.filling) and volume <= from_tank.filling:
            self.pour_water(volume)
            from_tank.pour_out_water(volume)
            current_operation = Operation('transfer_water', datetime.now(), volume,
                                          True)
            self.history.append(current_operation)
        else:
            print('There is not enough water in the source tank or'
                  ' free space in the destination tank')
            current_operation = Operation('transfer_water', datetime.now(), volume,
                                          False)
            self.history.append(current_operation)


class Warehouse:
    def __init__(self, tanks: list = []):
        self.tanks = tanks

    def find_max_tank(self, relative=False):
        max_tank = 'There is no water in any tank'
        max_level = 0
        for tank in self.tanks:
            if relative:
                water_level = tank.filling / tank.capacity
            else:
                water_level = tank.filling
            if water_level > max_level:
                max_tank = tank
                max_level = water_level
        return max_tank

    def find_empty_tanks(self):
        empty = []
        for tank in self.tanks:
            if tank.filling == 0:
                empty.append(tank.name)
        return empty

    def find_most_failing_tank(self):
        most_failing_tank = 'No fails'
        highest_fails_number = 0
        for tank in self.tanks:
            current_fails_number = 0
            for operation in tank.history:
                if operation.success:
                    current_fails_number += 1
            if current_fails_number > highest_fails_number:
                highest_fails_number = current_fails_number
                most_failing_tank = tank
        return most_failing_tank

    def find_most_x_operations_tank(self, kind_of_operation: str):
        '''
        Ta metoda jest bardzo podobna strukturą do poprzedniej, istotnie różnią się
        tylko na etapie warunku if operation.success /
        if operation.name == kind_of_operation - jak to uprościć do jednej metody?
        '''
        most_x_operations_tank = 'No operations of this kind'
        highest_x_operations_number = 0
        for tank in self.tanks:
            current_x_operations_number = 0
            for operation in tank.history:
                if operation.name == kind_of_operation:
                    current_x_operations_number += 1
            if current_x_operations_number > highest_x_operations_number:
                highest_x_operations_number = current_x_operations_number
                most_x_operations_tank = tank
        return most_x_operations_tank

    def check_state(self, tank: Tank):
        water_level = 0
        for operation in tank.history:
            if operation.success:
                if operation.name == 'pour_out_water':
                    water_level -= operation.water_amount
                else:
                    water_level += operation.water_amount
        return tank.filling == water_level


def main():
    first_tank = Tank('first_tank', 5)
    second_tank = Tank('second_tank', 10)
    third_tank = Tank('third_tank', 15)
    warehouse = Warehouse([first_tank, second_tank, third_tank])
    print(first_tank.name)
    print(first_tank.capacity)
    print(first_tank.filling)
    print(first_tank.history)
    first_tank.pour_water(3)
    print(first_tank.filling)
    print(first_tank.history)
    first_tank.pour_water(3)
    second_tank.pour_water(5)
    third_tank.pour_water(1)
    third_tank.pour_out_water(4)
    first_tank.transfer_water(third_tank, 4)
    first_tank.transfer_water(third_tank, 1)
    print(warehouse.find_empty_tanks())
    print(warehouse.find_max_tank())
    print(warehouse.find_most_failing_tank())
    print(warehouse.find_max_tank())
    print(warehouse.find_max_tank(relative=True))


if __name__ == '__main__':
    main()
