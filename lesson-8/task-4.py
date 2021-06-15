from functools import wraps


def val_checker(callback):
    def _val_checker(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if not callback(*args):
                raise ValueError('wrong val {0}'.format(*args))
            return function(*args, **kwargs)

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(j):
    return j ** 3


print(calc_cube)
print(calc_cube(5))
