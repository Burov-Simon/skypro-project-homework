import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

logger.info("Запуск модуля masks.py")


def get_mask_card_number(number_card: int = None) -> str:
    """Функция маскировки номера банковской карты"""
    logger.info("Запуск функции get_mask_card_number")
    if number_card is None:
        logger.error("Номер карты не указан!")
        return "Номер карты не указан"

    if not isinstance(number_card, int):
        logger.error("Номер должен состоять из цифр")
        raise TypeError("Номер должен состоять из цифр")

    if len(str(number_card)) != 16 or number_card < 0:
        logger.error("Номер должен состоять из 16 цифр")
        return "Номер должен состоять из 16 цифр"

    # переводим номер карты в строку и маскируем цифры
    logger.info("Переводим номер карты в строку и маскируем цифры")
    str_number_card = str(number_card)[:6] + "******" + str(number_card)[-4:]

    # создаем список и через цикл делим строку по 4 символа и добавляем в список
    list_number_card = []
    for i in range(0, len(str_number_card), 4):
        list_number_card.append(str_number_card[i: i + 4])

    # обьединяем список через пробел и выводим результат
    logger.info("Функция выполнена успешно!")
    return " ".join(list_number_card)


def get_mask_account(account_number: int = None) -> str:
    """Функция маскировки номера счета"""
    logger.info("Запуск функци get_mask_account")
    if account_number is None:
        logger.error("Номер счета не указан")
        return "Номер счета не указан"

    if not isinstance(account_number, int):
        logger.error("Номер должен состоять из цифр")
        raise TypeError("Номер должен состоять из цифр")

    if len(str(account_number)) != 20 or account_number < 0:
        logger.error("Номер должен состоять из 20 цифр")
        return "Номер должен состоять из 20 цифр"

    # переводим номер карты в строку и маскируем цифры
    logger.info("Функция выполнена успешно!")
    masked_account = "**" + str(account_number)[-4:]
    return masked_account
