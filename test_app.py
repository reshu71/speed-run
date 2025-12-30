import pytest
from process_users import get_average_age

# Test Case 1: The Happy Path
def test_average_basic():
    users = [
        {"meta": "age:20"},
        {"meta": "age:30"}
    ]
    # (20 + 30) / 2 = 25
    assert get_average_age(users) == 25

# Test Case 2: The "Dave" Bug (Zero Age)
def test_average_ignores_zero():
    users = [
        {"meta": "age:20"},
        {"meta": "age:0"}, # This should be ignored
        {"meta": "age:40"}
    ]
    # (20 + 40) / 2 = 30. (If bug exists, it would be 60/3 = 20)
    assert get_average_age(users) == 30