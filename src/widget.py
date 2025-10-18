from src.masks import get_mask_account, get_mask_card_number


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


def get_date(date_str: str) -> str:
    """Функция которвя возвращает дату ввиде ДД.ММ.ГГГГ"""
    date = date_str[:10].split("-")
    return ".".join(date[::-1])
