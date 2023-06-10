import json

data = json.load(open('data.json'))

print('Interface Status')
print('================================================================================')
print('DN' + '\t\t\t\t\t\t\t\t\t\t\t\t\t' + 'Description' + '\t\t\t' + 'Speed' + '\t' + 'MTU')
print('-------------------------------------------------- --------------------  ------  ------')
for elt in enumerate(data['imdata']):
    attributes = data['imdata'][elt[0]]['l1PhysIf']['attributes']
    print(attributes['dn'] + '\t\t\t' +
    attributes['descr'] + '\t\t\t\t\t' +
    attributes['speed'] + '\t\t' +
    attributes['attributes']['mtu'])
