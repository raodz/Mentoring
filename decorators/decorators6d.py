class Example:
    some_attribute = 'some attribute'

    def __init__(self):
        pass

    @classmethod
    def get_some_attribute(cls):
        return cls.some_attribute


# Test

print(Example.get_some_attribute())
