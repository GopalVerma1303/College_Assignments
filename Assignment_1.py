#Ans1:
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
n3=int(input("Enter the third number:"))
a=(n1+n2+n3)/3
print("The average is:", a)

#Ans2:
n1=int(input("Enter the gross income:"))
n2=int(input("Enter the number of dependents:"))
tax_rate=0.20
standard_deduction=10000
dependent_deduction=3000
taxable_income=n1-standard_deduction-dependent_deduction*n2
tax=taxable_income*tax_rate
print("The tax is:", tax)

#Ans3:
seconds=int(input("Enter the number of seconds:"))
n1=seconds//60
n2=seconds%60
print(n1,"minutes and", n2, "seconds")

#Ans4.
n1=25
n2='25'
n3=25.0
n2_int=int(n2)
n3_int=int(n3)
n4=n1+n2_int+n3_int
n5=str(n4)
print(n5)
type(n5)

#Ans5:
from math import pi,sin,cos
deg=0
y=0
z=0
for deg in range(0,346,15):
rad= deg*(pi/180)
y=round(sin(rad),4)
z=round(cos(rad),4)
print("sin",deg,"=",y,"and cos",deg,"=",z)
