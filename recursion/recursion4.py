def get_dict_depth(dictionary: dict, depth: int = 1):
    for key in dictionary:
        if type(dictionary[key]) == dict:
            depth += 1
            get_dict_depth(dictionary[key], depth)
    return depth


dict1 = {'value': [1, 2, 3, 4]}
dict2 = {'value': {'value2' : [1, 2, 3, 4]}}

print(get_dict_depth(dict1))
print(get_dict_depth(dict2))
