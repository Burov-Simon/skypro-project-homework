import os

import pytest

from src.decorators import log


@pytest.fixture
def clean_log_file():
    """Фикстура для очистки лог-файла перед тестами."""
    if os.path.exists("mylog.txt"):
        os.remove("mylog.txt")


def test_log(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(2, "3")
    result = capsys.readouterr()
    assert str(result.out) == "my_function error: TypeError. Inputs: (2, '3'), {}\n"
    assert my_function(2, 3) == 5


def test_log_file_success():
    @log("mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(2, 3)

    # Проверка записи в лог
    with open("mylog.txt", "r", encoding="utf-8") as file:
        log_content = file.read()

    assert "my_function ok" in log_content
    assert "Результат: 5" in log_content
    if os.path.exists("mylog.txt"):
        os.remove("mylog.txt")


def test_log_file_error():
    # Проверка записи ошибки в лог
    @log("mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(2, "3")
    with open("mylog.txt", "r", encoding="utf-8") as file:
        log_content = file.read()

    assert "my_function error: TypeError. Inputs: (2, '3'), {}" in log_content
    if os.path.exists("mylog.txt"):
        os.remove("mylog.txt")
