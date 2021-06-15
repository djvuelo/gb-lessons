from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        _func_args = ', '.join(map(lambda val: f'{val}: {str(type(val))}', [*args]))
        _func_kwargs = ', '.join(map(lambda val: f'{val[0]}: {str(type(val[1]))}', [*kwargs.items()]))
        _func_all = ', '.join([_func_args, _func_kwargs])
        return f'{func.__name__}({_func_all})  ->  {result}: {type(result)}'

    return wrapper


@type_logger
def calc_cube(x, y, test):
    return x ** 3


print(calc_cube(5, 8, test='rvefrvsv'))
