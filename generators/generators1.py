def some_generator():
    yield 'first value'
    yield 'second value'
    yield 'third value'


gen = some_generator()

print(next(gen))
print(gen.__next__())

for val in gen:
    if val == 'third value':
        gen.throw(ValueError('This is the last value'))
