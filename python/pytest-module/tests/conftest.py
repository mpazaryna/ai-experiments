import agent.shapes as shapes
import pytest


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)


@pytest.fixture
def flubba_rectangle():
    return shapes.Rectangle(5, 6)
