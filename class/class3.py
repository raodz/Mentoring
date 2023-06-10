class Rectangle:
    def __init__(self, length_: float, width_: float):
        self.length = length_
        self.width = width_

    def get_area(self):
        return self.width * self.length

    def get_circumference(self):
        return 2*(self.width + self.length)


def main():
    some_rec = Rectangle(4, 5)

    print(some_rec.get_area())
    print((some_rec.get_circumference()))


if __name__ == '__main__':
    main()
