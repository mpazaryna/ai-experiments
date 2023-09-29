year = int(input("Which year do you want to check? "))

# To determine a leap year, follow these steps:
# on every year that is evenly divisible by 4
#   except every year that is evenly divisible by 100
#     unless the year is also evenly divisible by 400

val1 = year % 4
val2 = year % 100
val3 = year % 400

if val1 == 0:
    if val2 == 0:
        if val3 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
