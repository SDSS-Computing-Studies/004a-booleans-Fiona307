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
if float(a) + float(b) >float(c) and float(b) + float(c) > float(a) and float(a) + float(c) >float(b):
    if a >= b:
        if c >= a:
            hypotenuse = math.sqrt(float(a)**2 + float(b)**2)
            if abs(float(hypotenuse) - float(c)) <= 0.02*float(c):
                print("that is a right triangle")
            elif float(hypotenuse) > float(c):
                print("that is an obtuse triangle")
            else:
                print("that is an acute triangle")
        else:
            hypotenuse = math.sqrt(float(c)**2 + float(b)**2)
            if abs(float(hypotenuse) - float(a)) <= 0.02*float(a):
                print("that is a right triangle")
            elif float(hypotenuse) > float(a):
                print("that is an obtuse triangle")
            else:
                print("that is an acute triangle")
    if b >= c:
        if a >= b:
            hypotenuse = math.sqrt(float(b)**2 + float(c)**2)
            if abs(float(hypotenuse) - float(a)) <= 0.02*float(a):
                print("that is a right triangle")
            elif float(hypotenuse) - float(a) > 0:
                print("that is an obtuse triangle")
            else:
                print("that is an acute triangle")
        else:
            hypotenuse = math.sqrt(float(c)**2 + float(a)**2)
            if abs(float(hypotenuse) - float(b)) <= 0.02*float(b):
                print("that is a right triangle")
            elif float(hypotenuse) - float(b) > 0:
                print("that is an obtuse triangle")
            else:
                print("that is an acute triangle")
    if c >= a:
        if b >= c:
            hypotenuse = math.sqrt(float(a)**2 + float(c)**2)
            if abs(float(hypotenuse) - float(b)) <= 0.02*float(b):
                print("that is a right triangle")
            elif float(hypotenuse) - float(b) > 0:
                print("that is an obtuse triangle")
            else:
                print("that is an acute triangle")
        else:
            hypotenuse = math.sqrt(float(b)**2 + float(a)**2)
            if abs(float(hypotenuse) - float(c)) <= 0.02*float(c):
                print("that is a right triangle")
            elif float(hypotenuse) - float(c) > 0:
                print("that is an obtuse triangle")
            else:
                print("that is an acute triangle")