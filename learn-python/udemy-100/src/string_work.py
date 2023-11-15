def greet():
    """Prints multiple hello messages."""
    print("hello, world\nhello\nhello to you too")


def concatenate_hello():
    """Concatenates and prints "hello" and "world"."""
    print("hello" + " " + "world")


def get_name():
    """Asks user for their name and returns it."""
    x = input("Enter your name: ")
    return x


def greet_user(name):
    """Greets the user with their name."""
    print("Hello, " + name)


def name_length(name):
    """Prints the number of characters in the user's name."""
    y = len(name)
    print("Your name has " + str(y) + " characters")


def main():
    """Main function to execute all other functions."""
    greet()
    concatenate_hello()
    name = get_name()
    greet_user(name)
    name_length(name)


# Call the main function to execute the code.
if __name__ == "__main__":
    main()
