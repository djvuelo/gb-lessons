class NumericListValueError(Exception):
    """exeption for NumericList class"""

    def __init__(self):
        super().__init__('Value of list error: must be int or float')


class NumericList:
    """List data type control class"""

    def __init__(self):
        self.__num_list = []

    def append(self, number):

        if number.isdigit():
            self.__num_list.append(number)
        else:
            try:
                self.__num_list.append(float(number))
            except ValueError:
                raise NumericListValueError

    def __str__(self):
        return str(self.__num_list)


if __name__ == '__main__':
    num_list = NumericList()
    while True:
        num = input('Введите целое число или "stop" для остановки:')
        if num == 'stop':
            print(num_list)
            break
        try:
            num_list.append(num)
        except NumericListValueError as error:
            print(error)
