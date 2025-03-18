import pytest
from src.decorators import log
from typing import Any



def test_log():
    @log()
    def my_function(x, y):
        return x + y
    result = my_function(1, 5)
    assert result == 6


def test_success_case_in_file():
    args = (1, "2")

    @log(filename="test.txt")
    def some_func(x, y):
        return x + y

    some_func(*args)
    with open("test.txt", "r", encoding="utf-8") as f:
        assert f.readlines()[-1] == f"{some_func.__name__} error: {TypeError}. Inputs:{args}"

def test_success_case_in_console(capsys):
    args = (1, "2")

    @log()
    def some_func(x, y):
        return x + y

    some_func(*args)
    assert capsys.readouterr().out == f"{some_func.__name__} error: {TypeError}. Inputs:{args}\n"


def test_success_case(capsys):
    args = (1, 2)

    @log()
    def some_fun(x, y):
        return x + y

    some_fun(*args)
    assert capsys.readouterr().out == f"some_fun ok\n"