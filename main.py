#import json
from datetime import datetime

from src.utils import load_transactions


print(
    """Привет! Добро пожаловать в программу работы с банковскими транзакциями. Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
)
ger = input("Введите цифру:")
if ger == "1":
    print("Для обработки выбран JSON-файл")
    print("""Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    her = input("Введите статус:")
    HER = her.upper()
    if HER == "EXECUTED":
        print("Операции отфильтрованы по статусу EXECUTED")
        filtrters = [req for req in load_transactions() if 'EXECUTED' in str(req) ]
        print("Отсортировать операции по дате? Да/Нет")
        answer = input()
        if answer == "Да":
            print("Отсортировать по возрастанию или по убыванию? Да/Нет")
            gerhtar = input()
            if gerhtar == "Да":
                otfil = sorted(filtrters, key=lambda x:datetime.strptime(x["date"], "%Y-%m-%d"), reverse=True)
            elif gerhtar == "Нет":
                otfil = sorted(filtrters,key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"), reverse=False)
        elif answer == "Нет":
            otfil = filtrters
            print("Выводить только рублевые тразакции? Да/Нет")
            terfrf = input()
            if terfrf == "Да":
                fhry = [gft for gft in filtrters if gft.get["operationAmount"]["currency"]["code"] == 'RUB']
                print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
                gdb = input()
                if gdb == "Да":
                    sorturovrf = [gft1 for gft1 in fhry if gft1.get["operationAmount"]["currency"]["code"] == 'RUB']
                elif gdb == "Нет":
                    sorturovrf = fhry
            elif terfrf == "Нет":
                fhry = filtrters

    else:
        print(f"Статус операции {HER} недоступен")
elif ger == "2":
    print("Для обработки выбран CSV-файл")
elif ger == "3":
    print("Для обработки выбран XLSX-файл")