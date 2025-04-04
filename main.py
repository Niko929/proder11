#import json
from datetime import datetime

from src.utils import load_transactions
from src.trans import tabl_nreg,tabl_ger


print(
    """Привет! Добро пожаловать в программу работы с банковскими транзакциями. Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
)
ger = input("Введите цифру:")
if ger == "1":
    transactions = load_transactions("data/operations.json")
    print("Для обработки выбран JSON-файл")
elif ger == "2":
        transactions = tabl_nreg("data/transactions.csv")
        print("Для обработки выбран CSV-файл")
elif ger == "3":
        transactions = tabl_ger("data/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл")
else:
    # если пользователь выбрал что-то некорректно, то по умолчанию можно открыть JSON-файл
    transactions = load_transactions("data/operations.json")
print("""Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
her = input("Введите статус:")
HER = her.upper()
if HER in ["EXECUTED", "CANCELED", "PENDING"]:
    print(f"Операции отфильтрованы по статусу {HER}")
    filtrter = [req for req in transactions if req.get('state') == HER]
else:
    print(f"Некорректный статус{HER}")


print("Отсортировать операции по дате? Да/Нет")
answer = input()
if answer == "Да":
    print("Отсортировать по возрастанию или по убыванию? Да/Нет")
    gerhtar = input()
    if gerhtar == "Да":
        otfil = sorted(filtrter, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"), reverse=False)
    elif gerhtar == "Нет":
        otfil = sorted(filtrter, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"), reverse=True)
elif answer == "Нет":
      otfil = filtrter

# Фильтрация только рублевых транзакций
print("Выводить только рублевые транзакции? Да/Нет")
terfrf = input()
if terfrf == "Да":
    fhry = [gft for gft in otfil if gft.get("operationAmount", {}).get("currency", {}).get("code") == 'RUB']
else:
    fhry = otfil

# Фильтрация по слову в описании (если требуется)
print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
gdb = input()
if gdb == "Да":
    keyword = input("Введите слово для фильтрации: ")
    sorturovrf = [gft1 for gft1 in fhry if keyword.lower() in gft1.get('description', '').lower()]
else:
    sorturovrf = fhry

# Вывод результатов
print(sorturovrf)