from exeptions import DivError


def div(a, b):
    """Division func a/b"""
    if b == 0:
        raise DivError(b)
    else:
        return a / b


'''
Simple test
'''
try:
    print(div(1, 0))
except DivError as error:
    print(error)

try:
    print(div(1, 56))
except DivError as error:
    print(error)

try:
    print(div(0, 56))
except DivError as error:
    print(error)
