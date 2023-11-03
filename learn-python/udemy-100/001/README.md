# Day One

## Band Name Generator

1. Create a greeting for your program.
2. Ask the user for the city that they grew up in.
3. Ask the user for the name of a pet.
4. Combine the name of their city and pet and show them their band name.
5. Make sure the input cursor shows on a new line

## GPT Prompt to get band generator code

I am writing writing a band name generator. The program should ask the user for the city they grew up in and the name of a pet.  It should then combine the two and print the band name. The program should also print a greeting. Make sure the input cursor shows on a new line.

Create a python program that will accomplish the task.  Add comments around every line and provide
a separate unit test file.  The unit test file should test every function in the program. The unit test file should be named test_band_name.py and the program file should be named band_name.py.  The program should be able to be executed at the command line. The program should be able to be tested by running python test_band_name.py at the command line. The program should be able to be imported by running import band_name.py at the python command line.

## Use of @patch

The line `@patch('builtins.input', return_value='John')` is a decorator from the `unittest.mock` module of the Python standard library. The purpose of this decorator is to mock (or temporarily replace) a built-in or external function during testing.

Let's break it down:

1. `@patch`: This is the decorator that is used to replace the real function with a mock object.

2. `'builtins.input'`: This is the target that we want to mock. In this case, we want to mock the built-in `input` function. The string `'builtins.input'` refers to the `input` function that exists in the `builtins` module (which is where many of Python's built-in functions are located).

3. `return_value='John'`: This is an argument to the `patch` function. It specifies the value that the mock object (in this case, the mock `input` function) should return when it's called. By setting `return_value='John'`, we're saying that whenever the `input` function is called in the function we're testing, it should return the string `'John'` without actually waiting for any real user input.

By using this decorator before a test function, we can simulate user input without having to actually input anything. This is useful for automating and running tests without manual intervention.

In the provided test, the `test_get_name` function is decorated with `@patch('builtins.input', return_value='John')`, which means that when `get_name()` calls `input()`, it will immediately return `'John'` without waiting for the user to type anything. This makes the test predictable and repeatable.
