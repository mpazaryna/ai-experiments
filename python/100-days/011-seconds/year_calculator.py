def seconds_in_year(years=1, leap_year=False):
    """
    Calculate the number of seconds in a year.

    Parameters:
    - years (int): Number of years to calculate for. Default is 1.
    - leap_year (bool): Whether the year is a leap year or not. Default is False.

    Returns:
    - int: Number of seconds in the specified number of years.
    """
    days_in_year = 366 if leap_year else 365
    seconds_in_day = 24 * 60 * 60
    return days_in_year * seconds_in_day * years
