seconds = int(input('Введите секунды:'))
duration = seconds
idx = 0

dictionary = [[60, ' сек. '],
              [60, ' мин. '],
              [24, ' час. '],
              [7, ' дн. '],
              [4, ' нед. '],
              [12, ' мес. '],
              [100, '(лет)год. '],
              [10, ' век. '],
              [100000, ' тыс-лет. ']]
answer = ''
while duration // dictionary[idx][0] != 0:

    next_duration = duration // dictionary[idx][0]
    this_duration = duration % dictionary[idx][0]

    if this_duration != 0:
        answer = f"{this_duration}{dictionary[idx][1]}{answer}"

    if next_duration // dictionary[idx + 1][0] == 0:
        answer = f"{next_duration}{dictionary[idx + 1][1]}{answer}"

    duration = next_duration
    idx += 1

print(f"{seconds} секунд это -> {answer}")
