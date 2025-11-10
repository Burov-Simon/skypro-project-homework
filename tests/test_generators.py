from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)


# Тест функции filter_by_currency()
# тест на проверку фильтрации транзакции по заданной валюте.
def test_filter_by_currency(transact: list) -> None:
    expected_transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]
    usd_transactions = filter_by_currency(transact, "USD")
    assert list(usd_transactions) == expected_transactions


# тест на пустой список и неправильную валюту
def test_filter_without_or_wrong_currency(transact: list) -> None:
    empty_transaction = filter_by_currency([])
    assert list(empty_transaction) == []
    wrong_currency = filter_by_currency(transact, "USDa")
    assert list(wrong_currency) == []


# Тест функции transaction_descriptions()
# тест для возвращения корректных описаний для каждой транзакции.
def test_transaction_descriptions(transact: list) -> None:
    expected_transactions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    desc_transaction = transaction_descriptions(transact)
    assert list(desc_transaction) == expected_transactions


# тест на пустой список
def test_transaction_descriptions_empty(transact: list) -> None:
    empty_transactions = transaction_descriptions([])
    assert list(empty_transactions) == []


# Тест функции card_number_generator()
# тест выдачи правильных номеров карт в заданном диапазоне.
def test_card_number_generator():
    expected_number_card = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    card_number = card_number_generator(1, 5)
    assert list(card_number) == expected_number_card


# тест на обработку крайних значений диапазона
def test_card_number_generator_range():
    start = 9999
    end = 10001
    generated_cards = card_number_generator(start, end)

    expected_cards = [
        "0000 0000 0000 9999",
        "0000 0000 0001 0000",
        "0000 0000 0001 0001",
    ]

    assert list(generated_cards) == expected_cards
