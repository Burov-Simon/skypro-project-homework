import pytest

#правильный номер карты
@pytest.fixture
def valid_card_number():
    return 7000792289606361

#правильная замаскированная карта
@pytest.fixture
def masked_card_number():
    return '7000 79** **** 6361'

#номер карты состоящий из символов
@pytest.fixture
def invalid_card_number_symbol():
    return 'qwertyuiopasdfgh'

#номер карты превышающий 16 цифр
@pytest.fixture
def invalid_card_number_long():
    return 1234567890123456789

#номер карты меньше 16 цифр
@pytest.fixture
def invalid_card_number_short():
    return 1234567890

@pytest.fixture
def invalid_card_number_empty():
    return None