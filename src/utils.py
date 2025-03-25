import json
import os
import requests
from dotenv import load_dotenv


def load_transactions(bar=None):
    """Загружает транзакции из JSON-файла."""
    with open(bar, "r", encoding="utf-8") as file:
        try:
            if bar:
                data = json.load(file)
                return data
            else:
                return []
        except Exception:
            return []


load_dotenv()  # Загружаем переменные окружения из .env

API_KEY = os.getenv("EXCHANGE_API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data"

def convert_transaction_to_rub(transaction: dict) -> float:
    # Ваш API ключ
    API_KEY = 'YOUR_API_KEY'  # Замените YOUR_API_KEY на ваш реальный API ключ

    # Получаем сумму и валюту из словаря
    amount = float(transaction["operationAmount"]["amount"])
    currency_code = transaction["operationAmount"]["currency"]["code"]

    # URL для запроса курса обмена
    url = f'https://api.apilayer.com/exchangerates_data/latest?base={currency_code}&symbols=RUB'

    # Заголовки для аутентификации
    headers = {
        'apikey': API_KEY
    }

    # Выполняем запрос к API
    response = requests.get(url, headers=headers)

    # Проверяем статус ответа
    if currency_code == "RUB":
        return amount
    elif response.status_code == 200:
        data = response.json()
        # Получаем курс обмена
        exchange_rate = data['rates']['RUB']
        amount_in_rub = amount * exchange_rate
        print(f"Сумма в рублях: {amount_in_rub:.2f} RUB")
    else:
        print("Ошибка при получении данных обмена:", response.status_code)

