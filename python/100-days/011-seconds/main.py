from year_calculator import seconds_in_year


def main():
    years = int(input("Enter the number of years: "))
    is_leap = input("Is it a leap year? (yes/no): ").strip().lower() == "yes"
    print(
        f"The number of seconds in {years} year(s) is: {seconds_in_year(years, is_leap)}"
    )


if __name__ == "__main__":
    main()
