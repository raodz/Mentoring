bill_items = [
    ['Tom', 'Calamari', 6.00],
    ['Tom', 'American Hot', 11.50],
    ['Tom', 'Chocolate Fudge Cake', 4.45],
    ['Clare', 'Bruschetta Originale', 5.35],
    ['Clare', 'Fiorentina', 10.65],
    ['Clare', 'Tiramisu', 4.90],
    ['Rich', 'Bruschetta Originale', 5.35],
    ['Rich', 'La Reine', 10.65],
    ['Rich', 'Honeycomb Cream Slice', 4.90],
    ['Rosie', 'Garlic Bread', 4.35],
    ['Rosie', 'Veneziana', 9.40],
    ['Rosie', 'Tiramisu', 4.90],
]
final_bill = {}

for order in bill_items:
    name, food, price = order
    if order[0] not in final_bill:
        final_bill[order[0]] = {'dishes': [order[1]], 'price': order[2]}
    else:
        final_bill[order[0]]['dishes'].append(order[1])
        final_bill[order[0]]['price'] += order[2]

print(final_bill)
