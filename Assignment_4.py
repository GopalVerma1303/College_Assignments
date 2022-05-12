#Ans1
print(bin(int(input("Enter a Number: "))))

#Ans2
print(eval(input("Enter the Expression: ")))

#Ans3

#a
print((3+4)*(5))

#b
n = int(input("Enter n: "))
print(n*(n-1)/2)

#c
from cmath import pi
r = int(input("Enter Radius: "))
print(4 * pi * r * r)

#d
import math
r = int(input("Enter r: "))
a = int(input("Enter a(radians): "))
b = int(input("Enter b(radians): "))
left = r * math.cos(a) * math.cos(a)
right = r * math.sin(b) * math.sin(b)
print(math.sqrt(left+right))

#e
x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
y1 = int(input("Enter y1: "))
y2 = int(input("Enter y2: "))
print((y2-y1)/(x2-x1))

# Ans4:
# a) 0, 1, 2, 3, 4 
# b) 3, 4, 5, 6, 7, 8, 9
# c) 4, 7, 10
# d) 15, 13, 11, 9, 7
# e) no_solution

#Ans5
H = int(input("Enter number of Hydrogen atoms: "))
C = int(input("Enter number of Carbon atoms: "))
O = int(input("Enter number of Oxygen atoms: "))
print("Molecular Weight: ", (H*1.00794 + C*12.0107 + O*15.9994))
