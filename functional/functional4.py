lines = ['10000101011', '111111', '01010101010010', '011001100001', '001010101011']

correct_lines = list(filter(lambda line: '11' not in line, lines))
answer = len(correct_lines)

print(answer)
# Nie użyłem count() i nie mam pomysłu, gdzie w tym zadaniu mogłaby się przydać ta metoda
# "11" -> count
