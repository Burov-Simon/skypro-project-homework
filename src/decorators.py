import functools


def log(filename=None):
    """Декоратор для логирования"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\nРезультат: {result}\n"
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_message)
            else:
                print(log_message)

        return wrapper

    return decorator


@log("mylog.txt")
def my_function(x, y):
    return x + y


my_function(10, 2)
