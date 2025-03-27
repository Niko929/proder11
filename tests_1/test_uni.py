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
# @mock.patch('builtins.open', new_ly = mock.mock_open,read_data = 'operations.json')
# def test_load_transactions(mock_file):
#     file_name = '../data/operations.json'  # Укажите путь к файлу
#     res_ccf = load_transactions(file_name)
#     assert res_ccf == {'key': 'value'}

# @patch('data')
# def test_load_transactions(mock_file):
#     mock_file.return_value = {'key': 'value'}
#     assert load_transactions() == {'key': 'value'}



from unittest.mock import patch
import random

def get_random_number():
    return random.randint(0, 10)

@patch('random.randint')
def test_get_random_number(mock_random):
    mock_random.return_value = 5
    assert get_random_number() == 5