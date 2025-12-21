import logging
import os
from pathlib import Path

import pandas as pd

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("transaction_reader.py")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/transaction_reader.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

path_file_csv = Path.cwd() / "data" / "transactions.csv"
path_file_excel = Path.cwd() / "data" / "transactions_excel.xlsx"


def trans_reader_csv(file_path_csv):
    """Функция чтения csv файла"""
    logger.info("Запуск программы")
    try:
        df = pd.read_csv(file_path_csv)
        logger.info("Успешно!")
        return df.to_dict("records")
    except FileNotFoundError:
        logger.error("Файл не найден!")
        return []
    except Exception:
        logger.error("Ошибка при чтении CSV!")
        return []


def trans_reader_excel(file_path_excel):
    """Функция чтения excel файла"""
    logger.info("Запуск програмы")
    try:
        df = pd.read_excel(file_path_excel)
        logger.info("Успешно!")
        return df.to_dict("records")
    except FileNotFoundError:
        logger.error("Файл не найден!")
        return []
    except Exception:
        logger.error("Ошибка при чтении excel!")
        return []
