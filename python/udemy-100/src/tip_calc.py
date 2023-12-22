total_bill = input("Total bill: ")
tip = input("What is the tip percentage 10, 12 or 15? ")
customers = input("What is the number of people? ")

bill = float(total_bill)
tip_percent = float(tip) / 100
people = int(customers)
amount_per_person = (bill + bill * tip_percent) / people
final_amount = "{:.2f}".format(amount_per_person)

print(f"Each person should pay: ${final_amount}")
