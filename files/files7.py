with open('przyklad2.txt', 'r', encoding='utf-8') as file:
    result = ''
    for line in file.readlines():
        splitted_line = line.split(' ')
        result += splitted_line[0]
        for i in range(1, len(splitted_line)-1):
            if splitted_line[i] != splitted_line[i-1] != splitted_line[i-1]:  # Problem z backslashem
                result += ' ' + splitted_line[i]
    print(result)
