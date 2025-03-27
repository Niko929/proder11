from unittest import mock
from unittest.mock import mock_open
import os
from src.utils import load_transactions
from unittest.mock import patch



ex = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }


@patch('bar.load_from_file')  # Укажите правильный путь к функции, которую хотите замокировать
def test_load_transactions(self, mock_load_from_file):
        # Настройка возвращаемого значения для замокированной функции
        mock_load_from_file.return_value = {'key': 'value'}

        # Вызов тестируемой функции
        result = load_transactions()

        # Проверка результата
        assert result == {'key': 'value'}




from unittest.mock import patch
import random

def get_random_number():
    return random.randint(0, 10)

@patch('random.randint')
def test_get_random_number(mock_random):
    mock_random.return_value = 5
    assert get_random_number() == 5