class Student:
    def __init__(self, name_: str, subject_: str, year_: int):
        """ opis funkcji/klasy """
        self.name = name_
        self.subject = subject_
        self.year = year_

    def __str__(self):
        return ('My name is {} and I am {}th '
                'year student of {}.'.format(self.name, self.year, self.subject))


def main():
    smith = Student('Smith', 'law', 4)

    print(smith)


if __name__ == '__main__':
    main()
