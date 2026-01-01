import pytest
from unittest.mock import patch, Mock
from api_client import get_user_status

# We use the @patch decorator to intercept 'requests.get'
# 'mock_get' is the fake object we swap in.
@patch('api_client.requests.get')
def test_get_user_status_active(mock_get):
    # 1. ARRANGE: Configure the fake to behave like a successful API
    mock_response = Mock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    # 2. ACT: Call the real function
    result = get_user_status(123)

    # 3. ASSERT: The function logic worked, even though no internet was used
    assert result == "active"

@patch('api_client.requests.get')
def test_get_user_status_inactive(mock_get):
    # 1. ARRANGE: Configure the fake to fail (404 Not Found)
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    # 2. ACT
    result = get_user_status(123)

    # 3. ASSERT
    assert result == "inactive"
