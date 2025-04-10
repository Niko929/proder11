import pytest
from src.banr import filter_operations_by_description
from src.descriction import count_operations, count_operations_by_category


@pytest.fixture
def operations():
    return [{
        "id": 441945886,
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
    {
        "id": 41428829,
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    },
    {
        "id": 939719570,
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 587085106,
        "state": "EXECUTED",
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431"
    }
    ]


def test_filter_empty_search_string(operations):
    result = filter_operations_by_description(operations, 'Перевод')
    expected = [{
        "id": 441945886,
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
    {
        "id": 41428829,
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    },
    {
        "id": 939719570,
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }]
    assert len(result) == 3
    assert result == expected


@pytest.fixture
def transactions():
    return [
        {"id": 441945886, "description": "Перевод организации", "from": "Maestro 1596837868705199",
         "to": "Счет 64686473678894779589"},
        {"id": 41428829, "description": "Перевод организации", "from": "MasterCard 7158300734726758",
         "to": "Счет 35383033474447895560"},
        {"id": 939719570, "description": "Перевод организации", "from": "Счет 75106830613657916952",
         "to": "Счет 11776614605963066702"},
        {"id": 587085106, "state": "EXECUTED", "description": "Открытие вклада", "to": "Счет 41421565395219882431"}
    ]


def test_count_operations_by_category(transactions):
    categories = ["Перевод организации", "Открытие вклада"]
    result = count_operations_by_category(transactions, categories)

    expected_result = {
        "Перевод организации": 3,
        "Открытие вклада": 1
    }

    assert result == expected_result

@pytest.fixture
def transactionsis():
    return [
        {"id": 1, "description": "Перевод организации", "from": "Счет 123", "to": "Счет 456"},
        {"id": 2, "description": "Открытие вклада", "to": "Счет 789"},
        {"id": 3, "from": "Счет 321", "to": "Счет 654"},  # Без описания
        {"id": 4, "description": "Закрытие вклада", "to": "Счет 987"},
        {"id": 5}  # Без описания
    ]

def test_count_operations(transactions):
    result = count_operations(transactions)
    expected_result = 4  # Ожидаем, что будет три транзакции с описанием
    assert result == expected_result