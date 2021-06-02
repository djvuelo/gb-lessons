from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б'
]


tk = (i for i in zip_longest(tutors, klasses))
print(type(tk))

print(next(tk))
print(next(tk))
print(next(tk))
print(next(tk))
print(next(tk))
print(next(tk))
print(next(tk))
print(next(tk))
