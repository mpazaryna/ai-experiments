def get_user_input():
    name = input("What's your name? ").strip().lower()
    day_of_week = input("What day of the week is it today? ").strip().lower()
    favorite_things = (
        input("Tell me a few of your favorite things (comma-separated): ")
        .strip()
        .split(",")
    )
    return name, day_of_week, favorite_things


def generate_affirmation(name, day_of_week, favorite_things):
    days = {
        "monday": "Marvelous",
        "tuesday": "Terrific",
        "wednesday": "Wonderful",
        "thursday": "Thrilling",
        "friday": "Fantastic",
        "saturday": "Superb",
        "sunday": "Spectacular",
    }

    # Get the corresponding affirmation for the day of the week (default to "Awesome" for unknown days)
    affirmation = days.get(day_of_week, "Awesome")

    # Convert the user's favorite things list into a string separated by commas
    favorite_things_str = ", ".join(favorite_things)

    # Create a personalized message using concatenation
    message = f"Hey {name.title()}, have an {affirmation} {day_of_week.title()}!\n"
    message += f"I hope you enjoy your {day_of_week.title()} surrounded by {favorite_things_str.title()}."

    return message


def main():
    name, day_of_week, favorite_things = get_user_input()
    affirmation_message = generate_affirmation(name, day_of_week, favorite_things)
    print(affirmation_message)


if __name__ == "__main__":
    main()
