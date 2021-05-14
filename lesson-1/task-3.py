percent = input("Введите процент для склонения:")


def get_percent(percent):
    dictionary = ['процент', 'процента', 'процентов']
    percent_digits = list(str(percent))
    answer = ""

    if len(percent_digits) > 1:
        if int(percent_digits[-2]) == 1 or int(percent_digits[-1]) == 0:
            answer = f"{percent} {dictionary[2]}"
        elif int(percent_digits[-1]) == 1:
            answer = f"{percent} {dictionary[0]}"
        elif 1 < int(percent_digits[-1]) < 5:
            answer = f"{percent} {dictionary[1]}"
        else:
            answer = f"{percent} {dictionary[2]}"
    else:
        if int(percent_digits[-1]) == 1:
            answer = f"{percent} {dictionary[0]}"
        elif 1 < int(percent_digits[-1]) < 5:
            answer = f"{percent} {dictionary[1]}"
        else:
            answer = f"{percent} {dictionary[2]}"

    return answer


print(get_percent(percent))

print("Вывод от 1 до 20:")

for percent in range(21):
    if percent == 0:
        continue
    print(get_percent(percent))
