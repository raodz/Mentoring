def count_vowels(text: str, counter: dict = {}):
    if text == '':
        return counter
    if text[0] in ['a', 'e', 'i', 'o', 'u', 'y']:
        try:
            counter[text[0]] += 1
        except KeyError:
            counter[text[0]] = 1
    return count_vowels(text[1:], counter)


text = 'some text'

print(count_vowels(text))
