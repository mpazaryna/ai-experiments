# format_data.py


def add_ten(val):
    try:
        # Attempt to add 10 to the provided value
        return val + 10
    except TypeError:
        # Re-raise the TypeError if the input is not a number
        raise TypeError("The provided value must be a number.")
    except Exception as e:
        # Optionally, handle any other unexpected exceptions
        raise e


def divide(num1, num2):
    try:
        # Attempt to divide num1 by num2
        return num1 / num2
    except ZeroDivisionError:
        # Re-raise the ZeroDivisionError if num2 is 0
        raise ZeroDivisionError("num2 cannot be 0.")
    except Exception as e:
        # Optionally, handle any other unexpected exceptions
        raise e
