class Shape:
    def __init__(self, length):
        self.length = length

    def get_area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

    def get_area(self):
        return self.length * self.length

def main():
    some_shape = Shape(5)
    print(some_shape.get_area())
    some_square = Square(5)
    print(some_square.get_area())

if __name__ == '__main__':
    main()