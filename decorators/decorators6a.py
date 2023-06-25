class Example:
    def __init__(self, text: str):
        self.text = text

    @property
    def get_text(self):
        return self.text


# Test


some_object = Example('abc')
print(some_object.get_text)
