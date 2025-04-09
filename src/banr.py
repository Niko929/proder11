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
