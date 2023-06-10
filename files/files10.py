# Preparation

with open('dane.txt', 'r') as data:
    rows = data.readlines()
digital_rows = []
for row in rows:
    digital_rows.append([int(x) for x in row.split()])

# 10.1
import numpy as np

all_values = list(np.concatenate(digital_rows).flat)
darkest = min(all_values)
brightest = max(all_values)
print(f'Najciemniejszy piksel: {darkest}')
print(f'Najjaśniejszy piksel: {brightest}')

# 10.2
import itertools


def check_symmetry(lst):
    for i in range(0, int((len(lst) / 2))):
        if lst[i] != lst[int(len(lst) - i - 1)]:
            return False
    return True


def get_min_sym(rows):
    for number_of_removed_rows in range(len(rows)):
        all_row_idx = range(len(rows))
        combinations_of_idx = list(
            itertools.combinations(all_row_idx, number_of_removed_rows))
        for unwanted in combinations_of_idx:
            current_rows = rows.copy()
            for row_to_remove in sorted(unwanted, reverse=True):
                del current_rows[row_to_remove]
            if check_symmetry(current_rows):
                result = int(len(rows) - len(current_rows))
                return result
    return 'No possible symmetry with these rows'


example_rows = [[1, 2], [1, 3], [1, 3], [1, 4], [0], [1, 2]]

print(
    f'Liczba usuniętych wierszy konieczna do uzyskania symetrii: {get_min_sym(example_rows)}')

# na przykładzie działa, na właściwych danych wyskakuje MemoryError

# 10.3

contrasts_number = 0
for i, j in zip(range(200), range(320)):
    neighbours = []
    try:
        neighbours.append(digital_rows[i - 1][j])
    except IndexError:
        pass
    # Chciałem wszystkie try-except dać w pętli, ale to by wymagało
    # iterowania po nie zawsze istniejących indeksach
    try:
        neighbours.append(digital_rows[i + 1][j])
    except IndexError:
        pass
    try:
        neighbours.append(digital_rows[i][j - 1])
    except IndexError:
        pass
    try:
        neighbours.append(digital_rows[i][j + 1])
    except IndexError:
        pass
    for neighbour in neighbours:
        if abs(digital_rows[i][j] - neighbour) > 128:
            contrasts_number += 1
            break

print(f'Liczba kontrastów: {contrasts_number}')

# 10.4
transposed_rows = np.array(digital_rows).T.tolist()

max_line = 0
for row in transposed_rows:
    local_max_line = 0
    for i in range(1, len(row)):
        if row[i - 1] == row[i]:
            local_max_line += 1
            if local_max_line > max_line:
                max_line = local_max_line
        else:
            local_max_line = 0

print(f'Maksymalna długość linii pionowej: {max_line}')
