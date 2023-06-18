class StarsAdder:
    def __init__(self):
        pass

    def __call__(self, function):
        def wrapper(*args, **kwargs):
            stars_line = len(args[0]) * '*'
            final_text = f'{stars_line}\n{function(*args, **kwargs)}\n{stars_line}'
            return final_text

        return wrapper

@StarsAdder()
def get_text(text: str):
    return text

print(get_text('Some text'))
print(get_text('Some longer text'))