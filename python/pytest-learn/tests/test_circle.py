import math

import agent.shapes as shapes
import pytest


class TestCircle:
    def setup_method(self, method):
        print(f"setup_method: {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"teardown_method {method}")

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius**2

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected

    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()
