# import json
#from datetime import datetime
from src.descriction import count_operations_by_category, count_operations
from src.utils import load_transactions
from src.gener import filter_by_currency
from src.trans import tabl_nreg, tabl_ger
from src.processing import sort_by_date, filter_by_state
from src.banr import filter_operations_by_description
from src.widget import get_date, mask_account_card

print(
    """Привет! Добро пожаловать в программу работы с банковскими транзакциями. Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
)
user_choice = input("Введите цифру:")
if user_choice == "1":
    transactions = load_transactions("data/operations.json")
    print("Для обработки выбран JSON-файл")
elif user_choice == "2":
    transactions = tabl_nreg("data/transactions.csv")
    print("Для обработки выбран CSV-файл")
elif user_choice == "3":
    transactions = tabl_ger("data/transactions_excel.xlsx")
    print("Для обработки выбран XLSX-файл")
else:
    # если пользователь выбрал что-то некорректно, то по умолчанию можно открыть JSON-файл
    transactions = load_transactions("data/operations.json")
print(
    """Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
)
state = input("Введите статус:").upper()
if state in ["EXECUTED", "CANCELED", "PENDING"]:
    print(f"Операции отфильтрованы по статусу {state}")
    transactions = filter_by_state(transactions, state)
else:
    print(f"Некорректный статус{state}")


print("Отсортировать операции по дате? Да/Нет")
answer = input().lower()
if answer == "да":
    print("Отсортировать по возрастанию или по убыванию? Да/Нет")
    reverse = input().lower()
    if reverse == "да":
        transactions = sort_by_date(transactions, reverse=False)
    elif reverse == "Нет":
        transactions = sort_by_date(transactions)
elif answer == "нет":
    transactions = transactions

# Фильтрация только рублевых транзакций

print("Выводить только рублевые транзакции? Да/Нет")
trans = input().lower()
if trans == "Да":
    filtered_rub_transactions = list(filter_by_currency(transactions))
else:
    filtered_rub_transactions = transactions


# Фильтрация по слову в описании (если требуется)
print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
filtering = input().lower()
if filtering == "да":
    keyword = input("Введите слово для фильтрации: ").lower()
    filtered_transactions = filter_operations_by_description(filtered_rub_transactions, keyword)
else:
    filtered_transactions = filtered_rub_transactions


for t in filtered_transactions:
    from_date = get_date(t['date'])
    if 'from' in t:
        ker1 = mask_account_card(t["from"])
    else:
        ker1 = "Информация о 'from' отсутствует."
    if 'to' in t:
        ker2 = mask_account_card(t["to"])
    else:
        ker2 = "Информация о 'to' отсутствует."

    if t["description"] == "Открытие вклада":
        print(f"{from_date} {t['description']}")
        print(ker2)
        print(f"Сумма: {t['operationAmount']['amount']} {t['operationAmount']['currency']['name']}\n")
    else:
        print(f"{from_date} {t['description']}")
        print(f"{ker1} -> {ker2}")
        print(f"Сумма: {t['operationAmount']['amount']} {t['operationAmount']['currency']['name']}\n")

category = ["Открытие вклада","Перевод со счета на счет","Перевод организации", "Перевод с карты на карту", ]
print(count_operations_by_category(filtered_transactions,category))

total_operations = count_operations(filtered_transactions)

if total_operations > 0:
        print(f"Найдено {total_operations} транзакций.")
else:
        print("Не найдено ни одной транзакции.")