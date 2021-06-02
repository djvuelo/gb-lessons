def odd_nums(num):
    return (_ for _ in range(1, num + 1))


odd_to_3 = odd_nums(3)
print(next(odd_to_3))
print(next(odd_to_3))
print(next(odd_to_3))
