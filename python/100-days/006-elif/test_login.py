import sys
import unittest
from io import StringIO

from login import login


class TestLogin(unittest.TestCase):
    def test_user1_login(self):
        # Prepare the input values
        input_values = ["user1", "pass1"]
        expected_output = "Welcome, User 1! Enjoy your day.\n"

        # Redirect sys.stdin to use our StringIO buffer and simulate user input
        sys.stdin = StringIO("\n".join(input_values))

        # Redirect sys.stdout to capture the program's output
        sys.stdout = StringIO()

        # Call the login function
        login()

        # Get the captured output
        actual_output = sys.stdout.getvalue()

        # Remove the input prompts from the actual output
        actual_output = actual_output.replace("Enter your username: ", "")
        actual_output = actual_output.replace("Enter your password: ", "")

        # Restore stdin and stdout
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Assert the output matches the expected output
        self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()
