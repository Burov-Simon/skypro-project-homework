from unittest.mock import Mock, patch

import pytest

from src.external_api import get_exchange


@pytest.fixture
def transaction_usd():
    return {"operationAmount": {"currency": {"code": "USD"}, "amount": "1000"}}


@pytest.fixture
def transaction_rub():
    return {"operationAmount": {"currency": {"code": "RUB"}, "amount": "1000"}}


@pytest.fixture
def transaction_invalid():
    return {"operationAmount": {"currency": {"code": "JPY"}, "amount": "1000"}}  # Некорректная валюта


@patch("src.external_api.requests.get")
def test_get_exchange_success(mock_get, transaction_usd):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 100}  # Пример возвращаемых данных
    mock_get.return_value = mock_response

    result = get_exchange(transaction_usd)

    assert result == {"result": 100}


@patch("src.external_api.requests.get")
def test_get_exchange_failure(mock_get, transaction_usd):
    mock_response = Mock()
    mock_response.status_code = 400
    mock_response.text = "Bad Request"
    mock_get.return_value = mock_response

    result = get_exchange(transaction_usd)

    assert result is None


def test_get_exchange_rub(transaction_rub):
    result = get_exchange(transaction_rub)

    assert result == "1000"


def test_get_exchange_invalid_currency(transaction_invalid):
    result = get_exchange(transaction_invalid)

    assert result == "Некорректная валюта"
