def get_generation(birth_year):
    if 1925 <= birth_year <= 1946:
        return "Traditionalists 🧓"
    elif 1947 <= birth_year <= 1964:
        return "Baby Boomers 🚀"
    elif 1965 <= birth_year <= 1981:
        return "Generation X 🎸"
    elif 1982 <= birth_year <= 1995:
        return "Millennials 📱"
    elif 1996 <= birth_year <= 2015:
        return "Generation Z 🧑‍💻"
    else:
        return "You are either from the future or too ancient to be classified! 😄"


def main():
    try:
        birth_year = int(input("Enter the year you were born: "))
        generation = get_generation(birth_year)
        print(f"You belong to {generation}")
    except ValueError:
        print("Invalid input. Please enter a valid year.")


if __name__ == "__main__":
    main()
