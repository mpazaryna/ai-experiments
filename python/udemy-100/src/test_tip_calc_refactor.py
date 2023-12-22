import unittest

from tip_calc_refactor import calculate_amount_per_person


class TestTipCalculator(unittest.TestCase):
    def test_calculate_bill(self):
        test_data = [
            {
                "total_bill": 100,
                "tip_percentage": 10,
                "num_of_people": 2,
                "expected_bill": "55.00",
            },
            {
                "total_bill": 200,
                "tip_percentage": 10,
                "num_of_people": 2,
                "expected_bill": "110.00",
            },
        ]

        for data in test_data:
            with self.subTest(data=data):
                self.assertEqual(
                    calculate_amount_per_person(
                        data["total_bill"],
                        data["tip_percentage"],
                        data["num_of_people"],
                    ),
                    data["expected_bill"],
                )


if __name__ == "__main__":
    unittest.main()
