class IsNotComplexNumber(Exception):
    """Исключение если введено не комплексное число"""

    def __init__(self, value):
        super().__init__(f'Error value ({value}): this is not complex number')


class Complex:
    """Класс по работе с комплексными числами"""

    def __init__(self, number):
        self._number = number

    @classmethod
    def number(cls, number):
        if not isinstance(number, complex):
            raise IsNotComplexNumber(number)
        return cls(number)

    def __mul__(self, other):
        return Complex(self._number * other._number)

    def __add__(self, other):
        return Complex(self._number + other._number)

    def __str__(self):
        return str(self._number)


try:
    cn1 = Complex.number(3 + 1j)
    cn2 = Complex.number(2 - 3j)
    print(cn1 * cn2)
    print(cn1 + cn2)
except IsNotComplexNumber as error:
    print(error)
