import pytest
from crypto import get_trading_signal
from unittest.mock import Mock,patch
import requests

@patch('crypto.requests.get')
def test_buy_signal(mock_get):
    response = Mock()
    response.status_code = 200
    response.json.return_value = {"price":35000}

    mock_get.return_value = response

    result = get_trading_signal(123)

    assert result == 'BUY'

@patch('crypto.requests.get')
def test_sell_signal(mock_get):
    response = Mock()
    response.status_code = 200
    response.json.return_value = {"price":65000}

    mock_get.return_value = response

    result = get_trading_signal(123)

    assert result == 'SELL'

@patch('crypto.requests.get')
def test_api_downtime(mock_get):
    response = Mock()
    response.status_code = 500
    response.json.return_value = {"price":65000}

    mock_get.return_value = response

    result = get_trading_signal(123)

    assert result == 'HOLD'

@patch('crypto.requests.get')
def test_network_crash(mock_get):

    mock_get.side_effect = requests.exceptions.ConnectionError

    result = get_trading_signal(123)

    assert result == 'NETWORK ERROR'



   

    
