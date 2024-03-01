def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "user1" and password == "pass1":
        print("Welcome, User 1! Enjoy your day.")
    elif username == "user2" and password == "pass2":
        print("Hello, User 2! Have a wonderful time.")
    elif username == "user3" and password == "pass3":
        print("Greetings, User 3! Hope you have an amazing day.")
    else:
        print("Invalid login credentials. Access denied.")

login()
