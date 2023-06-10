import json


def get_reversed_dict(**kwargs):
    return {v: k for k, v in kwargs.items()}


reversed_dict = get_reversed_dict(first_key='first_value', second_key='second_value')
reversed_json = json.dumps(reversed_dict)
print(reversed_json)
