summa = 0
summa_plus_17 = 0
cube_list = []

for number in range(1001):
    if number % 2 != 0:
        cube_number = number ** 3
        cube_list.append(cube_number)

for cube_number in cube_list:
    cube_number_plus_17 = cube_number + 17

    init_code_number = cube_number
    init_code_plus_17 = cube_number_plus_17

    summa_digits = 0
    summa_digits_plus_17 = 0

    while cube_number > 0:
        digit = cube_number % 10
        summa_digits += digit
        cube_number //= 10

    while cube_number_plus_17 > 0:
        digit = cube_number_plus_17 % 10
        summa_digits_plus_17 += digit
        cube_number_plus_17 //= 10

    if summa_digits % 7 == 0:
        summa += init_code_number

    if summa_digits_plus_17 % 7 == 0:
        summa_digits_plus_17 += init_code_plus_17

print(f"Cумма чисел из этого списка "
      f"(состоящий из кубов нечётных чисел от 0 до 1000),"
      f" сумма цифр которых делится нацело на 7: {summa}")

print(f"Cумма чисел из этого списка "
      f"(состоящий из кубов нечётных чисел от 0 до 1000 и прибавить 17),"
      f" сумма цифр которых делится нацело на 7: {summa_digits_plus_17}")
