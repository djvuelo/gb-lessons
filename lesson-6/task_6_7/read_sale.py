from sys import argv


def read_sale(from_line=1, to_line=None):
    with open('bakery.csv', 'r', encoding='UTF-8') as sales:
        sales.seek(14 * (from_line - 1))
        for sale in sales:
            print(f'ID {from_line}: {sale.strip().replace(".", ",")}')

            if to_line:
                if from_line == to_line:
                    break

            from_line += 1


if __name__ == '__main__':
    if len(argv) == 2:
        read_sale(int(argv[1]))
    elif len(argv) == 3:
        read_sale(int(argv[1]), int(argv[2]))
    else:
        read_sale()
