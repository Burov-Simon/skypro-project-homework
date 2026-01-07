from unittest.mock import mock_open, patch

import pandas as pd

from src.transaction_reader import trans_reader_csv, trans_reader_excel

trans_test_value = [
    {
        "id": 207126257,
        "state": "EXECUTED",
        "date": "2019-07-15T11:47:40.496961",
        "operationAmount": {"amount": "92688.46", "currency": {"name": "USD", "code": "USD"}},
        "description": "Открытие вклада",
        "from": "Счет 46363668439560358409",
        "to": "Счет 35737585785074382265",
    },
    {
        "id": 957763565,
        "state": "EXECUTED",
        "date": "2019-01-05T00:52:30.108534",
        "operationAmount": {"amount": "87941.37", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 46363668439560358409",
        "to": "Счет 18889008294666828266",
    },
    {
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {"amount": "97853.86", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612",
    },
]


def test_trans_reader_csv_success():
    df = pd.DataFrame(trans_test_value)
    with patch("src.transaction_reader.pd.read_csv", return_value=df):
        result = trans_reader_csv("any.csv")
    assert result == trans_test_value


def test_trans_reader_csv_file_not_found(caplog):
    with patch("src.transaction_reader.open", side_effect=FileNotFoundError, create=True):
        result = trans_reader_csv("missing.csv")
    assert result == []
    assert any("Файл не найден!" in rec.message for rec in caplog.records)


def test_trans_reader_csv_error(caplog):
    m = mock_open(read_data="bad,data")
    with patch("src.transaction_reader.open", m, create=True):
        with patch("src.transaction_reader.pd.read_csv", side_effect=ValueError("parse error")):
            result = trans_reader_csv("bad.csv")

    assert result == []
    assert any("Ошибка при чтении CSV!" in rec.message for rec in caplog.records)


def test_trans_reader_excel_success():
    df = pd.DataFrame(trans_test_value)
    with patch("src.transaction_reader.pd.read_excel", return_value=df):
        result = trans_reader_excel("any.excel")
    assert result == trans_test_value


def test_trans_reader_excel_file_not_found(caplog):
    with patch("src.transaction_reader.open", side_effect=FileNotFoundError, create=True):
        result = trans_reader_excel("missing.xlsx")
    assert result == []
    assert any("Файл не найден!" in rec.message for rec in caplog.records)


def test_trans_reader_excel_error(caplog):
    m = mock_open(read_data="bad,data")
    with patch("src.transaction_reader.open", m, create=True):
        with patch("src.transaction_reader.pd.read_excel", side_effect=ValueError("parse error")):
            result = trans_reader_excel("bad.excel")

    assert result == []
    assert any("Ошибка при чтении excel!" in rec.message for rec in caplog.records)
