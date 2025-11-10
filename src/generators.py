from itertools import chain
from typing import Iterable


def filter_by_currency(transactions: list, currency: str = None) -> Iterable:
    """Функция которая принимает на вход список словарей, представляющих транзакции.
    Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
        except KeyError:
            pass


def transaction_descriptions(transactions: list) -> Iterable:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, end: int) -> Iterable:
    """Генератор  который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X— цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001
    до 9999 9999 9999 9999."""
    for n in range(start, end + 1):
        num_card = str(n).zfill(16)
        finish_num_card = [num_card[0:4], num_card[4:8], num_card[8:12], num_card[12:]]
        n += 1
        yield " ".join(chain(finish_num_card))
