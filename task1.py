#! python3

# Have the user input a number. 
# Determine if the number is larger than 100 
# If it is, the output should read "The number is larger than 100" 
# (2 points)
# Inputs:
# number

# Outputs:
# "The number is larger than 100"
# "The number is smaller than 100"
# "The number is 100"

number = input("Enter a number")
larger = float(number) > 100
smaller = float(number) < 100
equal = float(number) == 100

if larger:
    print("The number is larger than 100")
if smaller:
    print("The number is smaller than 100")
if equal:
    print("The number is 100")