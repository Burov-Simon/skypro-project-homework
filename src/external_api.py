import os

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()
api_key = os.getenv("API_KEY")


def get_exchange(transaction):
    """Функция конвертации валюты"""
    if transaction["operationAmount"]["currency"]["code"] in ["USD", "EUR"]:
        money_to = "RUB"
        money_from = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={money_to}&from={money_from}&amount={amount}"

        headers = {"apikey": api_key}

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result
        else:
            print(f"Ошибка: {response.status_code} - {response.text}")
            return None
    elif transaction["operationAmount"]["currency"]["code"] == "RUB":
        return transaction["operationAmount"]["amount"]
    else:
        return "Некорректная валюта"
