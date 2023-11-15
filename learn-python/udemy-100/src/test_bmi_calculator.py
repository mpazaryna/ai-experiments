import unittest

from bmi_calculator import (  # Assuming your original file is named 'bmi_calculator.py'
    bmi_classification,
    calculate_bmi,
)


class TestBMICalculator(unittest.TestCase):
    def test_calculate_bmi_metric(self):
        # Test cases for metric measurements
        test_data = [
            {"height": 1.80, "weight": 70, "expected_bmi": 21},
            {"height": 1.60, "weight": 50, "expected_bmi": 19},
            {"height": 1.75, "weight": 75, "expected_bmi": 24},
        ]

        for data in test_data:
            with self.subTest(data=data):
                self.assertEqual(
                    calculate_bmi(data["height"], data["weight"], is_metric=True),
                    data["expected_bmi"],
                )

    def test_calculate_bmi_imperial(self):
        # Test cases for imperial measurements
        test_data = [
            {
                "height": 70.87,
                "weight": 154.32,
                "expected_bmi": 21,
            },  # equivalent of 1.80m and 70kg
            {
                "height": 62.99,
                "weight": 110.23,
                "expected_bmi": 19,
            },  # equivalent of 1.60m and 50kg
            {
                "height": 68.90,
                "weight": 165.35,
                "expected_bmi": 24,
            },  # equivalent of 1.75m and 75kg
        ]

        for data in test_data:
            with self.subTest(data=data):
                self.assertEqual(
                    calculate_bmi(data["height"], data["weight"], is_metric=False),
                    data["expected_bmi"],
                )

    def test_bmi_classification(self):
        # Test cases for BMI classifications
        classification_data = [
            {"bmi": 15, "expected": "Underweight (Severe thinness)"},
            {"bmi": 16.5, "expected": "Underweight (Moderate thinness)"},
            {"bmi": 17.5, "expected": "Underweight (Mild thinness)"},
            {"bmi": 20, "expected": "Normal range"},
            {"bmi": 28, "expected": "Overweight (Pre-obese)"},
            {"bmi": 32, "expected": "Obese (Class I)"},
            {"bmi": 37, "expected": "Obese (Class II)"},
            {"bmi": 42, "expected": "Obese (Class III)"},
        ]

        for data in classification_data:
            with self.subTest(data=data):
                self.assertEqual(bmi_classification(data["bmi"]), data["expected"])

    def test_zero_height(self):
        # This should raise a ZeroDivisionError since height is 0 for both metric and imperial
        with self.assertRaises(ZeroDivisionError):
            calculate_bmi(0, 70, is_metric=True)
        with self.assertRaises(ZeroDivisionError):
            calculate_bmi(0, 154.32, is_metric=False)

    # You can add more edge cases and tests as needed.


if __name__ == "__main__":
    unittest.main()
