import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тестирование правильности маскирования номера карты
def test_get_mask_card_number(valid_card_number: int, masked_card_number: int) -> None:
    assert get_mask_card_number(valid_card_number) == masked_card_number


# Проверка работы функции на различных входных форматах номеров карт,
# включая граничные случаи и нестандартные длины номеров.
def test_get_mask_card_number_incorrect(
    invalid_number_long: int, invalid_number_short: int, invalid_number_empty: None
) -> None:
    assert get_mask_card_number(invalid_number_long) == "Номер должен состоять из 16 цифр"
    assert get_mask_card_number(invalid_number_short) == "Номер должен состоять из 16 цифр"
    assert get_mask_card_number(invalid_number_empty) == "Номер карты не указан"


# Проверка, на входящий тип данных для карты
def test_get_mask_card_number_type(invalid_number_symbol: str) -> None:
    with pytest.raises(TypeError):
        get_mask_card_number(invalid_number_symbol)


# Тестирование правильности маскирования номера счета.
def test_get_mask_account(valid_account_number: int, valid_masked_account_number: str) -> None:
    assert get_mask_account(valid_account_number) == valid_masked_account_number


# Проверка работы функции с различными форматами и длинами номеров счетов.
def test_get_mask_account_incorrect(
    invalid_number_short: int, invalid_number_long: int, invalid_number_empty: None
) -> None:
    assert get_mask_account(invalid_number_long) == "Номер должен состоять из 20 цифр"
    assert get_mask_account(invalid_number_short) == "Номер должен состоять из 20 цифр"
    assert get_mask_account(invalid_number_empty) == "Номер счета не указан"


# Проверка на входящий тип данных для счета
def test_get_mask_account_type(invalid_number_symbol: str) -> None:
    with pytest.raises(TypeError):
        get_mask_account(invalid_number_symbol)
