class Tank:
    def __init__(self, name: str, capacity: float, filling: float = 0):
        self.name = name
        self.capacity = capacity
        self.filling = filling

    def pour_water(self, volume: float):
        if self.filling + volume <= self.capacity:
            self.filling += volume
        else:
            print('This amount of water will not fit in the tank')

    def pour_out_water(self, volume: float):
        if self.filling - volume >= 0:
            self.filling -= volume
        else:
            print('There is not as much water in the tank')

    def transfer_water(self, from_tank, volume: float):
        if volume <= (self.capacity - self.filling) and volume <= from_tank.filling:
            self.pour_water(volume)
            from_tank.pour_out_water(volume)
        else:
            print('There is not enough water in the source tank or'
                  ' free space in the destination tank')


class Warehouse:
    def __init__(self, tanks: list = []):
        self.tanks = tanks

    def find_max(self, relative = False):
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

    def find_empty(self):
        empty = []
        for tank in self.tanks:
            if tank.filling == 0:
                empty.append(tank)
        return empty

