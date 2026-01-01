import pytest
from unittest.mock import Mock,patch
from main_app import is_user_admin


@patch('main_app.get_user_from_db')
def test_admin_check_is_fast(mock_db_function):

    mock_db_function.return_value = {"id": 1, "username": "admin", "active": True}

    result = is_user_admin(1)

    assert result == True
    mock_db_function.assert_called_once_with(1)

@patch('main_app.get_user_from_db')
def test_db_crash(mock_db_function):
    mock_db_function.side_effect = ConnectionError("Boom!")

    result  = is_user_admin(99)

    assert result == 'System Down'