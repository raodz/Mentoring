def add_stars(function):
    def inner(*args, **kwargs):
        stars_line = len(args[0]) * '*'

        # Jak się zabezpieczyć przed tym, że argument z tekstem może mieć inny idx?
        final_text = f'{stars_line}\n{function(*args, **kwargs)}\n{stars_line}'
        return final_text

    return inner


@add_stars
def get_text(text: str):
    return text


print(get_text('Some text'))
print(get_text('Some longer text'))
