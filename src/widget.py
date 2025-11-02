from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция маскирующая номер карты или номер счета"""
    if not account_card or not account_card.strip():
        raise ValueError("Строка не должна быть пустой.")

    parts = account_card.strip().rsplit(" ", 1)
    if len(parts) != 2:
        raise ValueError("Некорректный формат строки. Ожидается 'Тип Номер'.")

    name_part, number_part = parts

    if not number_part.isdigit():
        raise ValueError("Номер должен содержать только цифры.")

    if len(number_part) == 20:
        masked_number = get_mask_account(int(number_part))
    else:
        masked_number = get_mask_card_number(int(number_part))

    return f"{name_part} {masked_number}"


def get_date(date_str: str) -> str:
    """Функция которая возвращает дату в виде ДД.ММ.ГГГГ"""
    if not date_str or len(date_str) < 10:
        raise ValueError("Входная строка должна содержать дату.")

    date = date_str[:10].split("-")
    if len(date) != 3 or not (date[0].isdigit() and date[1].isdigit() and date[2].isdigit()):
        raise ValueError("Входная строка должна содержать дату в формате 'YYYY-MM-DD'.")

    year, month, day = date

    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        raise ValueError("Входная строка должна содержать дату в формате 'YYYY-MM-DD'.")
    return ".".join(date[::-1])
