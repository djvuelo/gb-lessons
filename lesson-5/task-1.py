def odd_nums(num):
    for _ in range(1, num + 1):
        yield _


odd_to_3 = odd_nums(3)
print(next(odd_to_3))
print(next(odd_to_3))
print(next(odd_to_3))