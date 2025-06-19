from tasks import BracketValidator


def test_valid_cases():
    validator = BracketValidator()
    assert validator.is_valid("()[]{}") is True
    assert validator.is_valid("([{}])") is True
    assert validator.is_valid("") is True

def test_invalid_cases():
    validator = BracketValidator()
    assert validator.is_valid("([)]") is False
    assert validator.is_valid("(") is False
    assert validator.is_valid("({[}") is False
