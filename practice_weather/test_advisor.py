import pytest
from advisor import  get_clothing_advice
from unittest.mock import Mock,patch

@patch('advisor.fetch_weather')
def test_heatwave_advice(mock_get):

    response = Mock()

    response = {'temp': 35, 'condition': 'Sunny'}

    mock_get.return_value = response

    result = get_clothing_advice('Miami')

    assert result == "Wear Shorts"

@patch('advisor.fetch_weather')
def test_cold_snap_advice(mock_get):

    response = Mock()

    response = {'temp': 5, 'condition': 'Snow'}

    mock_get.return_value = response

    result = get_clothing_advice('Alaska')

    assert result == "Wear a Coat"

@patch('advisor.fetch_weather')
def test_api_failure(mock_weather):
    # 1. CONFIGURE THE EXPLOSION
    # We don't want data. We want the code to crash with a TimeoutError.
    mock_weather.side_effect = TimeoutError
    
    # 2. RUN THE CODE
    # When advisor.py calls fetch_weather(), it will blow up.
    # Your try/except block in advisor.py should catch it.
    result = get_clothing_advice('Nowhere')
    
    # 3. ASSERT
    assert result == "Stay Home"
    

    
    