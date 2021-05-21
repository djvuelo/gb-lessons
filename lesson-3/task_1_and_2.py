en_ru_nums = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять"
}


def num_translate(num):
    translate = en_ru_nums.get(num)
    if not translate:
        translate = en_ru_nums.get(num.lower())
        if translate:
            translate = translate.title()
    return translate


while 1:
    print(num_translate(input("Введите число на английском(например \"one\"):")))
