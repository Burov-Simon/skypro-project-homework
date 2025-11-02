import pytest


# правильный номер карты
@pytest.fixture
def valid_card_number():
    return 7000792289606361


# правильная замаскированная карта
@pytest.fixture
def masked_card_number():
    return "7000 79** **** 6361"


# номер состоящий из символов
@pytest.fixture
def invalid_number_symbol():
    return "qwertyuiopasdfgh"


# номер карты превышающий 16 цифр
@pytest.fixture
def invalid_number_long():
    return 12345678901234567890123456789


# номер карты меньше 16 цифр
@pytest.fixture
def invalid_number_short():
    return 1234567890


# пустое значение
@pytest.fixture
def invalid_number_empty():
    return None


# правильный номер счета
@pytest.fixture
def valid_account_number():
    return 73654108430135874305


# правильно замаскированный номер счета
@pytest.fixture
def valid_masked_account_number():
    return "**4305"
