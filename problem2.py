#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

number = input("Enter a number")
interger = float(number) == number

if interger:
    print("the number is an interger")
else:
    print("the number is not an integer")