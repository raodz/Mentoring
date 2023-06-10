import re

raw_data = 'starting value'
all_raw_data = []
while raw_data := input('Please provide data'):
    if re.search(r'.*[ ]\d+$', raw_data):
        all_raw_data.append(raw_data)
    else:
        print('Incorrect data')
sum_city_temp = {}
for elt in all_raw_data:
    city, temp = elt.split(' ')

    value = sum_city_temp.get(city, 0)
    value += int(temp)

print(sum_city_temp)
