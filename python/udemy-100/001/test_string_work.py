import unittest
from io import StringIO
from unittest.mock import patch

import string_work  # assuming the provided functions are in string_work.py


class TestStringWorkFunctions(unittest.TestCase):
    def test_greet(self):
        # Redirect standard output
        captured_output = StringIO()
        with patch("sys.stdout", new=captured_output):
            string_work.greet()
        self.assertEqual(
            captured_output.getvalue(), "hello, world\nhello\nhello to you too\n"
        )

    def test_concatenate_hello(self):
        # Redirect standard output
        captured_output = StringIO()
        with patch("sys.stdout", new=captured_output):
            string_work.concatenate_hello()
        self.assertEqual(captured_output.getvalue(), "hello world\n")

    @patch("builtins.input", return_value="John")
    def test_get_name(self, mock_input):
        self.assertEqual(string_work.get_name(), "John")

    def test_greet_user(self):
        # Redirect standard output
        captured_output = StringIO()
        with patch("sys.stdout", new=captured_output):
            string_work.greet_user("Jane")
        self.assertEqual(captured_output.getvalue(), "Hello, Jane\n")

    def test_name_length(self):
        # Redirect standard output
        captured_output = StringIO()
        with patch("sys.stdout", new=captured_output):
            string_work.name_length("Anna")
        self.assertEqual(captured_output.getvalue(), "Your name has 4 characters\n")


if __name__ == "__main__":
    unittest.main()
