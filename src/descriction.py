def count_operations_by_category(transactions, categories):
    # Инициализируем словарь для хранения результатов

    category_count = {category: 0 for category in categories}


    # Проходим по всем транзакциям
    for transaction in transactions:
        description = transaction.get("description")

        # Если описание операции находится в списке категорий, увеличиваем счетчик
        if description in category_count:
            category_count[description] += 1

    return category_count


def count_operations(transactions):
    # Инициализируем счетчик
    count = 0
    # Проходим по всем транзакциям
    for r in transactions:
        # Проверяем, есть ли описание операции в списке категорий
        if 'description' in r:
            count += 1
    return count

