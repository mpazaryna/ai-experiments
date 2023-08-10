from year_calculator import seconds_in_year


def test_non_leap_year():
    assert seconds_in_year() == 365 * 24 * 60 * 60


def test_leap_year():
    assert seconds_in_year(leap_year=True) == 366 * 24 * 60 * 60


def test_multiple_years():
    assert seconds_in_year(years=2) == 2 * 365 * 24 * 60 * 60


def test_multiple_leap_years():
    # Note: This test is hypothetical, as not all consecutive years can be leap years.
    assert seconds_in_year(years=2, leap_year=True) == 2 * 366 * 24 * 60 * 60


def test_hardcoded():
    assert seconds_in_year(years=1, leap_year=False) == 31536000
