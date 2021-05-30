from sys import argv
from add_sale import sale_fix_symbols
from read_sale import read_sale


def edit_sale(id, value):
    with open('bakery.csv', 'r+') as sales:
        sales.seek(14 * (id - 1))
        sales.write(sale_fix_symbols(value))


if __name__ == '__main__':
    if len(argv) == 3:
        edit_sale(int(argv[1]), argv[2])
        read_sale()
