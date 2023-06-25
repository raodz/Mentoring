from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass
    '''Bez abstractmethod działa tak samo - czemu to służy?'''


class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def get_area(self) -> float:
        area = (self.base * self.height) / 2
        return area


# Test

some_triangle = Triangle(4, 3)
print(some_triangle.get_area())