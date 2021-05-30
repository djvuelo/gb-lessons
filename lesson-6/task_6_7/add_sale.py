from sys import argv
from read_sale import read_sale


def sale_fix_symbols(price):
    price = float(price.replace(',', '.'))
    if price > 9999999999.99:
        print('Максимальная сумма 9999999999.99')
        exit(1)
    return f'{price // 1:10.0f}.{(price % 1) * 100:02.0f}\n'


def add_sale(value):
    sales = open('bakery.csv', 'a')
    sales.write(value)
    sales.close()
    read_sale()


if __name__ == '__main__':
    if len(argv) > 1:
        add_sale(sale_fix_symbols(argv[1]))
    else:
        print('Введите сумму')
