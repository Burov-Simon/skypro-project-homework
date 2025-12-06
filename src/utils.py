import json
import logging
import os
from pathlib import Path

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("utils.py")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

path_file_json = Path.cwd() / "data" / "operations.json"


logger.info("Запуск модуля utils.py")


def get_file_operations(path):
    """Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях"""
    logger.info("Запуск программы!")
    try:
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if not isinstance(data, list):
                    logger.error("Данные в файле не являются списком!")
                    return []
                logger.info("Функция выполнена успешно!")
                return data
            except json.decoder.JSONDecodeError:
                logger.error("Ошибка чтении файла!")
                return []
    except FileNotFoundError:
        logger.error("Файл не найден!")
        return []
