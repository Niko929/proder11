import re

from src.utils import load_transactions


def filter_operations_by_description(operations, search_string):
    # Компилируем регулярное выражение для поиска
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)  # Игнорируем регистр

    # Фильтруем операции по описанию
    filtered = [
        operation
        for operation in operations
        if "description" in operation and pattern.search(operation["description"])
    ]

    return filtered


# Пример использования
# operations_data = load_transactions("../data/operations.json")
#
# search_term = "перевод"
# filtered_results = filter_operations_by_description(operations_data, search_term)
#
# print(filtered_results)
