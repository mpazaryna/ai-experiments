def get_user_input():
    userName = input("What is your name? ")
    favoriteFood = input("What is your favorite food? ")
    favoriteMusic = input("What is your favorite music? ")
    return userName, favoriteFood, favoriteMusic


def print_output(userName, favoriteFood, favoriteMusic):
    print("Hello, " + userName + ".")
    print("Your hungry for " + favoriteFood + " right?")
    print("Put on some " + favoriteMusic + " and eat the feast.")
    print("you are awesome!")


def main():
    userName, favoriteFood, favoriteMusic = get_user_input()
    print_output(userName, favoriteFood, favoriteMusic)


if __name__ == "__main__":
    main()
