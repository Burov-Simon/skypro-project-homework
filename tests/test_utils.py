import json
from unittest.mock import mock_open, patch

from src.utils import get_file_operations

sample_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 50}]
json_text = json.dumps(sample_data)


def test_returns_list_on_valid_json():
    m = mock_open(read_data=json_text)
    with patch("src.utils.open", m, create=True):
        result = get_file_operations("any.json")
    assert result == sample_data


def test_returns_empty_on_malformed_json(capsys):
    m = mock_open(read_data="not a json")
    with patch("src.utils.open", m, create=True):
        result = get_file_operations("any.json")
    captured = capsys.readouterr()
    assert result == []
    assert "Ошибка чтении файла" in captured.out


def test_returns_empty_if_data_not_list(capsys):
    m = mock_open(read_data=json.dumps({"id": 1}))
    with patch("src.utils.open", m, create=True):
        result = get_file_operations("any.json")
    captured = capsys.readouterr()
    assert result == []
    assert "Данные в файле не являются списком" in captured.out


def test_returns_empty_on_file_not_found(capsys):
    def fake_open(*args, **kwargs):
        raise FileNotFoundError

    with patch("src.utils.open", fake_open, create=True):
        result = get_file_operations("missing.json")
    captured = capsys.readouterr()
    assert result == []
    assert "Файл не найден!" in captured.out
