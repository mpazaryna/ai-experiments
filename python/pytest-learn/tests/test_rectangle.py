import agent.shapes as shapes
import pytest


def test_area():
    rectangle = shapes.Rectangle(10, 20)
    assert rectangle.area() == 10 * 20


def test_perimeter():
    rectangle = shapes.Rectangle(10, 20)
    assert rectangle.perimeter() == (10 * 2) + (20 * 2)


def test_area_fixture(my_rectangle):
    assert my_rectangle.area() == 10 * 20


def test_not_equal(my_rectangle, flubba_rectangle):
    assert my_rectangle != flubba_rectangle
