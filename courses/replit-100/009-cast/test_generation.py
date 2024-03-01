from generation import get_generation


def test_get_generation():
    # Test cases for different birth years and expected generations
    test_cases = [
        (1925, "Traditionalists 🧓"),
        (1947, "Baby Boomers 🚀"),
        (1965, "Generation X 🎸"),
        (1982, "Millennials 📱"),
        (1999, "Generation Z 🧑‍💻"),
        (2010, "Generation Z 🧑‍💻"),
        (2025, "You are either from the future or too ancient to be classified! 😄"),
        (3000, "You are either from the future or too ancient to be classified! 😄"),
    ]

    for birth_year, expected_generation in test_cases:
        result = get_generation(birth_year)
        assert (
            result == expected_generation
        ), f"Failed for birth year {birth_year}. Expected: {expected_generation}, Got: {result}"
