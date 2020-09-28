#! python3 

# Have the user enter a number. 
# Use an if...elif statement to determine if the number is 
# a) larger than 1000 
# b) larger than 100 
# c) larger than 10 
# d) larger than 0 
# Output must match one of the valid output statements listed
# (2 points)

# Inputs:
# a number

# Output is a single number that represents a range of numbers:
# "3" : The number is equal to 1000 or is larger than 1000
# "2" : The number is 100 or a number up to 1000 
# "1" : The number is 10 or a number up to 100 
# "0" : The number is 0 or a number up to 100 

number = input("Enter a number")
a = float(number) >= 1000
b = float(number) >= 100
c = float(number) >= 10
d = float(number) >= 0

if a:
    print("3")
elif b:
    print("2")
elif c:
    print("1")
elif d:
    print("0")