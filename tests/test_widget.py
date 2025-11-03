import pytest

from src.widget import mask_account_card, get_date


# Тест mask_account_card()
# Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки
# в зависимости от типа входных данных (карта или счет).
@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(account_card: str, expected: str) -> None:
    assert mask_account_card(account_card) == expected


# Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.
def test_non_digit_number() -> None:
    with pytest.raises(ValueError):
        mask_account_card("Visa Platinum 1234abc")


def test_empty_string() -> None:
    with pytest.raises(ValueError):
        mask_account_card("")


# Тест get_date()
# Тестирование правильности преобразования даты.
@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2000-01-01T12:00:00", "01.01.2000"),
        ("1999-12-31T23:59:59", "31.12.1999"),
    ],
)
def test_valid_date(date_str: str, expected: str) -> None:
    assert get_date(date_str) == expected


# Проверка, что функция корректно обрабатывает входные строки
def test_incorrect_length() -> None:
    with pytest.raises(ValueError):
        get_date("")
    with pytest.raises(ValueError, match="Входная строка должна содержать дату."):
        get_date("2024")


def test_non_date_string() -> None:
    with pytest.raises(ValueError):
        get_date("Некорректная строка")
