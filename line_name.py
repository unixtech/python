import inspect


def __line__():
    return inspect.currentframe().f_back.f_lineno



print(f"I'm {__file__} on line {__line__()}!")
