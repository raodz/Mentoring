to_sort = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]


def sort_by_second(list_of_tuples):
    list_of_tuples.sort(key=lambda subjects: subjects[1])
    return list_of_tuples


print(sort_by_second(to_sort))
