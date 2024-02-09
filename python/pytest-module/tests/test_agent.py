import agent.agent as agent
import pytest


def test_add_ten():
    result = agent.add_ten(5)
    assert result == 15


def test_add_ten_with_string():
    with pytest.raises(TypeError) as excinfo:
        agent.add_ten("string")
    assert str(excinfo.value) == "The provided value must be a number."


def test_divide():
    result = agent.divide(10, 5)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as excinfo:
        agent.divide(10, 0)
    assert str(excinfo.value) == "num2 cannot be 0."
