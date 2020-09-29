#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"

import math

a = input ("Enter one side of a triangle")
b = input("Enter another side of the triangle")
c = input("Enter the third side of the triangle")
if a >= b:
    if c >= a:
        hypotenuse = math.sqrt(float(a)**2 + float(b)**2)
        if float(hypotenuse) - float(c) <= 0.02*float(c):
            print("that is a right triangle")
        elif float(hypotenuse) - float(c) < 0:
            print("that is an obtuse triangle")
        else:
            print("that is an acute triangle")
    else:
        hypotenuse = math.sqrt(float(c)**2 + float(b)**2)
        if float(hypotenuse) - float(a) <= 0.02*float(a):
            print("that is a right triangle")
        elif float(hypotenuse) - float(a) < 0:
            print("that is an obtuse triangle")
        else:
            print("that is an acute triangle")
elif b >= c:
    hypotenuse = math.sqrt(float(a)**2 + float(c)**2)
    if float(hypotenuse) - float(b) <= 0.02*float(b):
        print("that is a right triangle")
    elif float(hypotenuse) - float(b) < 0:
        print("that is an obtuse triangle")
    else:
        print("that is an acute triangle")
else:
    hypotenuse = math.sqrt(float(a)**2 + float(b)**2)
    if float(hypotenuse) - float(c) <= 0.02*float(c):
        print("that is a right triangle")
    elif float(hypotenuse) - float(c) < 0:
        print("that is an obtuse triangle")
    else:
        print("that is an acute triangle")