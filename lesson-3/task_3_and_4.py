def thesaurus(*args):
    name_sorting = {}
    for name in args:
        name_sorting.setdefault(name.split()[1][0], {}).setdefault(name.split()[0][0], []).append(name)
    return name_sorting


print(thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

'''
Результат:
{
    'С':
        {
            'И': ['Иван Сергеев', 'Инна Серова'],
            'А': ['Анна Савельева']
        },
    'А':
        {
            'П': ['Петр Алексеев']
        },
    'И':
        {
            'И': ['Илья Иванов']
        }
}
'''

