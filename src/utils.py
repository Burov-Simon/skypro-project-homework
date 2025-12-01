import json
from pathlib import Path


path_file_operations = Path.cwd() / 'data' / 'operations.json'

def get_file_operations(path_file_operations):
    """Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path_file_operations, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                if not isinstance(data, list):
                    print('Данные в файле не являются списком')
                    return []
                return data
            except json.decoder.JSONDecodeError:
                print('Ошибка чтении файла')
                return []
    except FileNotFoundError:
        print('Файл не найден!')
        return []

print(get_file_operations(path_file_operations))
