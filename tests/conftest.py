from typing import List, Dict, Any

import pytest


# правильный номер карты
@pytest.fixture
def valid_card_number() -> int:
    return 7000792289606361


# правильная замаскированная карта
@pytest.fixture
def masked_card_number() -> str:
    return "7000 79** **** 6361"


# номер состоящий из символов
@pytest.fixture
def invalid_number_symbol() -> str:
    return "qwertyuiopasdfgh"


# номер карты превышающий 16 цифр
@pytest.fixture
def invalid_number_long() -> int:
    return 12345678901234567890123456789


# номер карты меньше 16 цифр
@pytest.fixture
def invalid_number_short() -> int:
    return 1234567890


# пустое значение
@pytest.fixture
def invalid_number_empty() -> None:
    return None


# правильный номер счета
@pytest.fixture
def valid_account_number() -> int:
    return 73654108430135874305


# правильно замаскированный номер счета
@pytest.fixture
def valid_masked_account_number() -> str:
    return "**4305"


# словари для модуля processing.py
@pytest.fixture
def list_dicts() -> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_dicts_executed() -> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def list_dicts_canceled() -> List[Dict[str, Any]]:
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_dicts_descending() -> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def list_dicts_ascending() -> List[Dict[str, Any]]:
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
