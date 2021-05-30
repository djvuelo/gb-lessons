from sys import argv


def users_hobbies(users, hobbies):
    users_hobbies_dict = []
    with open(users, 'r') as users:
        with open(hobbies, 'r') as hobbies:
            for user in users:
                surname, name, lastname = user.rstrip().split(',')
                hobby = hobbies.readline()

                if hobby == '':
                    hobby = None

                '''
                Если 'Выращивание растений и цветов', то становится ['Выращивание растений', 'Выращивание цветов']
                Если 'Игры на компьютерах и приставках', то становится ['Игры на компьютерах', 'Игры на приставках']
                '''

                hobby = hobby.rstrip().split(' и ')
                if len(hobby) > 1:
                    if len(hobby[1].split(' ')) == 1 and len(hobby[0].split(' ')) > 1:
                        hobby_prefix = " ".join(hobby[0].split()[:-1:])
                        hobby[1] = f'{hobby_prefix} {hobby[1]}'
                    else:
                        hobby[1] = hobby[1].title()

                # выбрал словарь со списком хобби, для удобства пользоваться потом
                users_hobbies_dict.append(
                    {'fio': {'name': name, 'surname': surname, 'lastname': lastname}, 'hobby': hobby})

            print(users_hobbies_dict)

            exit(1)


if __name__ == '__main__':
    if len(argv) >= 3:
        users_hobbies(argv[1], argv[2])
    else:
        print('Укажите 2 файла с которых нужно парсить')
