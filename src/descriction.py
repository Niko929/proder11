from collections import Counter

def count_operations_by_category(transactions, categories):
    transactions_descriptions = [
        transaction.get("description", "")
        for transaction in transactions
        if transaction.get("description", "") in categories
    ]
    return dict(Counter(transactions_descriptions))



def count_operations(transactions):
    # Инициализируем счетчик
    count = 0
    # Проходим по всем транзакциям
    for r in transactions:
        # Проверяем, есть ли описание операции в списке категорий
        if 'description' in r:
            count += 1
    return count

