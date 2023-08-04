# test_summarizer.py

import unittest

from call_summarize import run_call_summarize


class TestRunCallSummarizeIntegration(unittest.TestCase):
    def test_run_call_summarize_integration(self):
        # Use a known URL (preferably some static content that doesn't change)
        test_url = "https://austinkleon.com/2010/01/31/logbook/"  # this is a real website, but its content is static and won't change

        # Run the function
        result = run_call_summarize(test_url)
        print(result)

        # Check the result
        self.assertIsNotNone(result)  # Ensure something is returned
        self.assertIsInstance(result, str)  # Ensure a string is returned
        # Optionally, check if the returned result contains some expected content or keywords
        # self.assertIn("some expected content", result)


if __name__ == "__main__":
    unittest.main()
