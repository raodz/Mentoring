from dataclasses import dataclass


@dataclass
class Example:
    first_attribute: int
    second_attribute: str


# Test

example = Example(0, 'abc')
print(example)
