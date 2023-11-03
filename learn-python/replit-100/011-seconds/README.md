# Seconds in a year

How many seconds are in a year?

## Pytest file naming (Follow the conventions)

The following is a completion from GPT4

In `pytest`, the conventional naming pattern for test files is to prefix them with `test_`. This convention is not just a matter of style; it has practical implications. When you run `pytest` without any arguments, it will discover and run all tests in files that match the pattern `test_*.py` or `*_test.py` in the current directory and its subdirectories.

If you name your test file as `get_function_test.py`, `pytest` will still discover and run the tests inside it because it matches the `*_test.py` pattern. However, if you name it `get_function_test.py` and it's located in a subdirectory, make sure that the subdirectory also has an `__init__.py` file, so it's recognized as a Python package/module.

On the other hand, if you name it `get_function_test.py`, it won't be automatically discovered by `pytest` because it doesn't match either of the conventional patterns.

In summary:

- `test_get_function.py`: This is the conventional naming pattern and will be automatically discovered by `pytest`.
- `get_function_test.py`: This will also be discovered by `pytest`, but it's slightly less conventional.

It's always a good idea to stick to conventions, especially when working in a team, as it makes the codebase more predictable and easier for others to understand. However, if you have a strong reason to deviate from the convention, you can, but you should ensure that your tests are still being discovered and run by `pytest`.
