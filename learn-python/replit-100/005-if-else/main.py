def identify_character():
    flexibility = input("Do you consider yourself flexible? (yes/no): ").lower()
    equanimity = input("Are you able to maintain equanimity in challenging situations? (yes/no): ").lower()

    if flexibility == "yes" and equanimity == "yes":
        print("Congratulations! You are a yogi.")
    else:
        print("You are not a yogi.")

# Call the function to run the identification
identify_character()