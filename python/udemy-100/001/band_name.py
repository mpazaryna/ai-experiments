# band_name.py


# This function gets the city from the user.
def get_city():
    city = input("\nPlease enter the city you grew up in: ")
    return city


# This function gets the pet name from the user.
def get_pet():
    pet = input("Please enter the name of a pet: ")
    return pet


# This function combines the city and pet name to form the band name.
def generate_band_name(city, pet):
    return city + " " + pet


def main():
    # Print a greeting to the user.
    print("Welcome to the Band Name Generator!")

    # Get the city and pet name.
    city = get_city()
    pet = get_pet()

    # Generate and print the band name.
    band_name = generate_band_name(city, pet)
    print(f"\nYour band name is: {band_name}")


if __name__ == "__main__":
    main()
