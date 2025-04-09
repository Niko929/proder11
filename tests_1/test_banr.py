#import unittest
from src.banr import filter_operations_by_description
from src.descriction import count_operations, count_operations_by_category


def test_filter_empty_search_string(self):
    result = filter_operations_by_description(self.operations, '')
    self.assertEqual(len(result), len(self.operations))

def test_count_operations_with_descriptions(self):
        result = count_operations(self.transactions)
        self.assertEqual(result, 4)


def test_count_operations_empty_transactions(self):
    result = count_operations_by_category([], self.categories)
    expected_result = {
        "Открытие вклада": 0,
        "Перевод средств": 0,
        "Оплата услуг": 0
    }
    self.assertEqual(result, expected_result)