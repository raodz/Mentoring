data = {
    'data': [1, 2, 'asd', [2, 3, 4, 5]],
    'nested_analysis': {
        'analysis_1': [1, 10, 15, 120.2, '120'],
        'analysis_2': [10, 100, 'test', 200, 300],
    },
    'probes': [['probe_1', 'probe_2'], 'probe_3']
}

unpacked_data = []

for elt in data.values():
    if type(elt) == str:
        unpacked_data.append(elt)
    elif type(elt) == list:
        unpacked_data += elt
    elif type(elt) == dict:
        unpacked_data += list(elt.values())


def flat2gen(alist):  # Copied function for flattening lists
    for item in alist:
        if isinstance(item, list):
            for subitem in item:
                yield subitem
    else:
        yield item


flat_list = (list(flat2gen(unpacked_data)))

str_list = [elm for elm in flat_list if isinstance(elm, str)]

print(str_list)
