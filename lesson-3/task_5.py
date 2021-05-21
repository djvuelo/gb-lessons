from random import randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count, unique=False):
    """
    The function will return random list of jokes

    Parameters:
    count (int): Count of jokes
    unique (bool): Repeat or don't repeat words from lists -> (default False)

    Returns:
    list: Random list of jokes

    Example:
    get_jokes(2) -> ["лес завтра зеленый", "город вчера веселый"]

    """
    jokes_list = []
    for _ in range(count):
        if unique:
            jokes_list.append(f'{nouns.pop(randrange(0, len(nouns)))} '
                              f'{adverbs.pop(randrange(0, len(adverbs)))} '
                              f'{adjectives.pop(randrange(0, len(adjectives)))}')
            if not nouns:
                break
        else:
            jokes_list.append(f'{nouns[randrange(0, len(nouns))]} '
                              f'{adverbs[randrange(0, len(adverbs))]} '
                              f'{adjectives[randrange(0, len(adjectives))]}')
    return jokes_list


print(str(get_jokes(count=2)), sep='\n')
