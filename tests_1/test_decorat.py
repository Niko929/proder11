import pytest
from src.decorators import log
from src.test import my_function


def test_log(Any):
    @log(function="my.txt")
    def my_function(x, y):
        return x + y

    result = my_function(1, 5)
    assert result == 6


@pytest.mark.parametrize('fr,fr2',[
    (1,2),('my_function ok'),
])

def test_dever(fr,fr2):
    assert log(fr) == fr2