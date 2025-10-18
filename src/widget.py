from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(account_card: str) -> str:
    """Функция маскирующая номер карты или номер счета"""
    count_digit = ""
    # определяем с помощью цикла карту или счет
    for num in account_card:
        if num.isdigit():
            count_digit += num
    # возвращаем замаскированные данные в зависимости от результата
    if len(count_digit) == 16:
        return account_card[:-16] + get_mask_card_number(int(count_digit))
    else:
        return account_card[:-20] + get_mask_account(int(count_digit))
