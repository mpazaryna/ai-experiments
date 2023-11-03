# You and your friends went to dinner and need to split the bill.
# Being the clever friend you are, you can use your code to discover
# how much each person owes.
#
# myBill is a float because the total bill will probably have a decimal point
# numberOfPeople is an int.


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")


print("Tip Calculator")

# Get input for the total bill
myBill = get_float_input("How much did you spend: ")

# Get input for the tip percentage
tip = get_float_input("How much did you want to tip (as a percentage): ")

# Get input for the number of people in the party
numberOfPeople = get_int_input("How many people are in your party: ")

try:
    # Calculate the total bill with the tip included
    tip /= 100
    total_bill = myBill + (myBill * tip)

    # Calculate the amount each person should pay
    if numberOfPeople > 0:
        total_bill_per_person = total_bill / numberOfPeople
        print(f"Each person should pay: ${total_bill_per_person:.2f}")
    else:
        print("Number of people should be greater than 0.")
except ZeroDivisionError:
    print("Number of people should be greater than 0.")
