# if / elif / else operator
print("welcome to the age classifier")
if (int(input("What is your age? "))) < 18:
    print("You are a child")
elif (int(input("What is your age? "))) < 65:
    print("You are an adult")
else:
    print("You are a senior")
