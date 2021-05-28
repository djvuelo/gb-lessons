from requests import get, utils
from sys import argv
from datetime import datetime


def currency_rates(code_valuta, fields=['value']):
    """
    :param code_valuta: code valuta
    :param fields: What fields get
    :return: dict with fields
    """
    result = {}
    we_have = str(code_valuta).upper()
    response = get("http://www.cbr.ru/scripts/XML_daily.asp")
    encoding = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encoding)

    if not we_have in content:
        return None

    dd, mm, yyyy = map(int, content.split('Date="')[1].split('"')[0].split('.'))
    valuta_info = content.split(we_have)[1]
    date = datetime(year=yyyy, month=mm, day=dd)

    result['date'] = date

    for field in fields:
        result[field] = valuta_info.split(f'<{field.title()}>')[1].split(f'</{field.title()}>')[0].replace(',', '.')
        if field == 'value':
            result[field] = float(result[field])

    return result


if __name__ == '__main__':
    if len(argv) > 1:
        currency = currency_rates(argv[1], fields=['nominal', 'name', 'value'])
        if currency:
            print(f'{currency["nominal"]} {currency["name"]} = {currency["value"]} Российских рублей, '
                  f'{currency["date"]:%Y-%d-%m}')
        else:
            print('Такой валюты нет.')
    else:
        print("Введите параметр (например USD)")
else:
    pass
