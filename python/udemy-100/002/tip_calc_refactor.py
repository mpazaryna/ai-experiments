# Refactored code
def calculate_amount_per_person(total_bill, tip_percentage, num_of_people):
    bill = float(total_bill)
    tip_percent = float(tip_percentage) / 100
    people = int(num_of_people)
    amount_per_person = (bill + bill * tip_percent) / people
    final_amount = "{:.2f}".format(amount_per_person)
    return final_amount


def main():
    total_bill = input("Total bill: ")
    tip_percentage = input("What is the tip percentage 10, 12 or 15? ")
    num_of_people = input("What is the number of people? ")

    final_amount = calculate_amount_per_person(
        total_bill, tip_percentage, num_of_people
    )

    print(f"Each person should pay: ${final_amount}")


if __name__ == "__main__":
    main()
