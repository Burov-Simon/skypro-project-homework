def get_mask_card_number(number_card: int = None) -> str:
    """Функция маскировки номера банковской карты"""
    if number_card is None:
        return "Номер карты не указан"

    if not isinstance(number_card, int):
        raise TypeError("Номер должен состоять из цифр")

    if len(str(number_card)) != 16 or number_card < 0:
        return "Номер должен состоять из 16 цифр"

    # переводим номер карты в строку и маскируем цифры
    str_number_card = str(number_card)[:6] + "******" + str(number_card)[-4:]

    # создаем список и через цикл делим строку по 4 символа и добавляем в список
    list_number_card = []
    for i in range(0, len(str_number_card), 4):
        list_number_card.append(str_number_card[i : i + 4])

    # обьединяем список через пробел и выводим результат
    return " ".join(list_number_card)


def get_mask_account(account_number: int = None) -> str:
    """Функция маскировки номера счета"""
    if account_number is None:
        return "Номер счета не указан"

    if not isinstance(account_number, int):
        raise TypeError("Номер должен состоять из цифр")

    if len(str(account_number)) != 20 or account_number < 0:
        return "Номер должен состоять из 20 цифр"

    # переводим номер карты в строку и маскируем цифры
    masked_account = "**" + str(account_number)[-4:]
    return masked_account
