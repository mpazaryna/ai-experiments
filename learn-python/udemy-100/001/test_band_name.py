# test_band_name.py

import unittest

import band_name


class TestBandNameGenerator(unittest.TestCase):
    # Test the get_city function.
    def test_get_city(self):
        # Since this function relies on user input, it's not straightforward to unit test.
        # Typically, you would mock the input function to simulate user input.
        pass

    # Test the get_pet function.
    def test_get_pet(self):
        # Same as get_city, this would require mocking.
        pass

    # Test the generate_band_name function.
    def test_generate_band_name(self):
        city = "New York"
        pet = "Whiskers"
        expected_band_name = "New York Whiskers"
        self.assertEqual(band_name.generate_band_name(city, pet), expected_band_name)


if __name__ == "__main__":
    unittest.main()
