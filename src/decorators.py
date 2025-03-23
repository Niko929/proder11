from functools import wraps


def log(filename=None):
    """
    Декоратор для логирования выполнения функций.
    """

    def her(fun):
        @wraps(fun)
        def ytr(*args, **kwargs):
            try:
                result = fun(*args, **kwargs)
                """Если файл написал, то значения записывает в него, если нет то запись выходит в консоль """
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"\n{fun.__name__} ok")
                else:
                    print(f"{fun.__name__} ok")
                return result
            except Exception as r:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"\n{fun.__name__} error: {type(r)}. Inputs:{args}")
                else:
                    print(f"{fun.__name__} error: {type(r)}. Inputs:{args}")
                return r

        return ytr

    return her
