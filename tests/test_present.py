import pytest

from lib.present import Present

"""
Item wrapped
Get it back when unwrapped
"""

def test_wrap_then_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33

"""
If unwrapped before wrapped
Get error msg
"""

def test_unwrap_error():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message = str(e.value)
    assert message == "No contents have been wrapped."

"""
If we try to wrap twice
Get error
"""
def test_wrap_twice():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
        message = str(e.value)
        assert message == "A contents has already been wrapped."