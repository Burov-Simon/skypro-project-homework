from typing import Any, Dict, List

from src.processing import (filter_by_state, process_bank_operations,
                            process_bank_search, sort_by_date)


# Тестирование функсии filter_by_state()
# Тестирование фильтрации списка словарей по заданному статусу state
def test_filter_by_state(
    list_dicts: List[Dict[str, Any]],
    list_dicts_executed: List[Dict[str, Any]],
    list_dicts_canceled: List[Dict[str, Any]],
) -> None:
    assert filter_by_state(list_dicts, "EXECUTED") == list_dicts_executed
    assert filter_by_state(list_dicts, "CANCELED") == list_dicts_canceled
    assert filter_by_state(list_dicts) == list_dicts_executed


# Проверка работы функции при отсутствии словарей с указанным статусом state в списке
def test_filter_by_state_no_matches(list_dicts: List[Dict[str, Any]]) -> None:
    assert filter_by_state(list_dicts, "UNDEFINED") == []


# Тестирование функции sort_by_date()
# Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
def test_sort_by_date_descending(
    list_dicts: List[Dict[str, Any]],
    list_dicts_descending: List[Dict[str, Any]],
    list_dicts_ascending: List[Dict[str, Any]],
) -> None:
    assert sort_by_date(list_dicts, descending=True) == list_dicts_descending
    assert sort_by_date(list_dicts, descending=False) == list_dicts_ascending


# Проверка корректности сортировки при одинаковых датах
def test_sort_by_date_with_same_dates() -> None:
    input_data = [
        {"id": 1, "date": "2022-01-01T10:00:00"},
        {"id": 2, "date": "2022-01-01T10:00:00"},
        {"id": 3, "date": "2022-01-02T09:00:00"},
    ]
    expected = [
        {"id": 3, "date": "2022-01-02T09:00:00"},
        {"id": 1, "date": "2022-01-01T10:00:00"},
        {"id": 2, "date": "2022-01-01T10:00:00"},
    ]
    assert sort_by_date(input_data) == expected


# Проверка на пустой список
def test_sort_by_date_empty() -> None:
    assert sort_by_date([]) == []


def test_process_bank_search():
    data = [
        {"description": "Перевод на карту"},
        {"description": "Оплата за интернет"},
        {"description": "Покупка в магазине"},
    ]

    result = process_bank_search(data, "перевод")
    assert len(result) == 1
    assert result[0]["description"] == "Перевод на карту"

    result = process_bank_search(data, "оплата")
    assert len(result) == 1
    assert result[0]["description"] == "Оплата за интернет"

    result = process_bank_search(data, "")
    assert len(result) == 3

    result = process_bank_search(data, "не существует")
    assert len(result) == 0


def test_process_bank_operations():
    data = [
        {"description": "Перевод на карту"},
        {"description": "Оплата за интернет"},
        {"description": "Перевод на карту"},
        {"description": "Покупка в магазине"},
    ]
    categories = ["Перевод на карту", "Оплата за интернет", "Неизвестная категория"]

    result = process_bank_operations(data, categories)
    assert result["Перевод на карту"] == 2
    assert result["Оплата за интернет"] == 1
    assert result["Неизвестная категория"] == 0
