import pytest

from lib.pw_checker import PasswordChecker

"""
Password incorrect length
"""

def test_bad_pw():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check("Hello")
    error = str(e.value)
    assert error == "Invalid password, must be 8+ characters."

"""
Password correct length
"""

def test_good_pw():
    checker = PasswordChecker()
    result = checker.check("password")
    assert result == True
