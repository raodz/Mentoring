def example1():
    for i in range(3):
        try:
            x = int(input("enter a number: "))
            y = int(input("enter another number: "))
            print(x, '/', y, '=', x / y)
        except ValueError:
            print('Both values must be integers')
        except ZeroDivisionError:
            print('The second value cannot be 0')


def example2(L):
    print("\n\nExample 2")
    sum = 0
    sumOfPairs = []
    try:
        for i in range(len(L)):
            sumOfPairs.append(L[i] + L[i + 1])
    except IndexError:
        print('The list must have at least two elements')
    except TypeError:
        print('All values in the list must be the same type')

    print("sumOfPairs = ", sumOfPairs)


def printUpperFile(fileName):
    file = open(fileName, "r")
    for line in file:
        print(line.upper())
    file.close()


def main():
    example1()
    L = [10, 3, 5, 6, 9, 3]
    example2(L)
    example2([10, 3, 5, 6, "NA", 3])
    try:
        example3([10, 3, 5, 6])
    except NameError:
        print('There is no such a function')

    try:
        printUpperFile("doesNotExistYest.txt")
        printUpperFile("./Dessssktop/misspelled.txt")
    except FileNotFoundError:
        print('Incorrect file name or incorrect directory')


if __name__ == '__main__':
    main()
