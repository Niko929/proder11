from functools import wraps


def log(function):
    def her(fun):
        @wraps(fun)
        def ytr(*args, **kwargs):
            try:
                result = fun(*args, **kwargs)
                if function is not None:
                    with open(function, "a") as file:
                        file.write(f"{fun.__name__} ok")
                    print(f"{fun.__name__} ok")
                else:
                    print(f"{fun.__name__} ok")
                return result
            except Exception as r:
                if function is not None:
                    with open(function, "a") as file:
                        file.write(f"{fun.__name__} error: {type(r)}. Inputs:{args}")
                    print(f"{fun.__name__} error: {r}. Inputs:{args}")
                else:
                    print(f"{fun.__name__} error: {r}. Inputs:{args}")
                raise r

        return ytr

    return her
