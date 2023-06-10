with open('test.txt', 'r') as file:
    for line_number in range(3):
        file.readline()
    print(file.readline())
