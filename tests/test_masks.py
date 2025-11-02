import pytest

from src.masks import get_mask_card_number


# Тестирование правильности маскирования номера карты
def test_get_mask_card_number(valid_card_number, masked_card_number):
    assert get_mask_card_number(valid_card_number) == masked_card_number

#Проверка работы функции на различных входных форматах номеров карт,
# включая граничные случаи и нестандартные длины номеров.
def test_get_mask_card_number_symbol(invalid_card_number_long, invalid_card_number_short, invalid_card_number_empty):
    assert get_mask_card_number(invalid_card_number_long) == 'Номер должен состоять из 16 цифр'
    assert get_mask_card_number(invalid_card_number_short) == 'Номер должен состоять из 16 цифр'
    assert get_mask_card_number(invalid_card_number_empty) == 'Номер карты пуст'


#Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты
def test_get_mask_card_number_type(invalid_card_number_symbol):
    with pytest.raises(TypeError):
        get_mask_card_number(invalid_card_number_symbol)