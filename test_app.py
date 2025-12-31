import pytest
from process_users import parse_age

# The "Strategy": List of (input, expected_output) tuples
test_cases = [
    ("age:30,role:admin", 30),  # Standard
    ("role:admin,age:45", 45),  # Different order
    ("role:guest", 0),          # Missing age
    ("age:0", 0),               # Zero age
    ("age:99,role:user", 99),   # High number
]

@pytest.mark.parametrize("meta_string","expected_string",test_cases)
def test_parse_age_variations(meta_string,expected_string):
    assert parse_age(meta_string) == expected_string