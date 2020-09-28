#! python3
# Have the user input a number 
# Determine if the number is positive, negative or 0 
# 2 points

# Inputs:
# number

# Outputs:
# - "positive"
# - "negative"
# - "zero"

number = input("Enter a number")
positive = float(number) > 0
negative = float(number) < 0
zero = float(number) == 0

if positive:
    print("positive")
if negative:
    print("negative")
if zero:
    print("zero")