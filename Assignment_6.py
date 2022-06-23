#Ans1
n = int(input("Enter a number: "))
s = 0
for i in range(1, n):
    if(n%i==0):
        s+=i
if(s==n):
    print("Perfect")
else:
    print("Not Perfect")

# Enter a number: 496
# Perfect

#Ans2
s = input("Enter Word: ")
s = s.lower()
s1 = s[::-1]
if(s==s1):
    print("Palindrome")
else:
    print("Not Palindrome")

# Enter Word: gopal
# Not Palindrome

#Ans3
from math import factorial
def getPascal(n):
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            print(factorial(i)//factorial(j)*factorial(i-j), end=" ")
        print()
n = int(input("Enter number of rows: "))
getPascal(n)

# Enter number of rows: 3
#     1 
#    1 1
#   1 2 1

#Ans4
ones = 0
a = [0 for i in range(26)]
s = input("Enter String: ")
ns = s.lower()
for i in s:
    i = ord(i)
    a[i-97]|=1
for i in a:
    ones+=i
if(ones==26):
    print("Pangram")
else:
    print("Not a Pangram")

# Enter String: abcdefghijklmnopqrstuvwxyz
# Pangram

#Ans5
def hyphenSort(str1, str2):
    words = str1.split("-")
    words.sort()
    for i in words:
        str2.append(i+"-")
    for j in range(0, len(str2),1):
        if(j==(len(str2)-1)):
            str3 = str2[j]
            str3 = str3[:-1]
            print (str3)
        else:
            print(str2[j], end="")
str0 = input("Enter hyphen separated string: ")
str2 = []
hyphenSort(str0, str2)
 
# Enter hyphen separated string: green-red-yellow-black-white
# Black-green-red-white-yellow
 
# Ans6
class Student:
    Id = 123
    Name = "Gopal Verma"
    Class = "L21"
 
def student_data(arg):
    if(arg=="student_id"):
        print(Student.Id)
    elif(arg=="student_name"):
        print(Student.Name)
    elif(arg=="student_class"):
        print(Student.Class)
 
arg = input()
student_data(arg)

# student_id
# 123
# student_name
# Gopal Verma
# student_class 
# L21

# Ans7
class Student:
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object)) 

# True
# False
# True
# False

# Check whether the said classes are subclasses of the built-in object class or not.
# True
# True

# Ans8
n = int(input())
arr = list(map(int, input("Enter array: ").strip().split()))[:n]
tempList = []
ansList = []
for i in range(1, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if((arr[i]+arr[j]+arr[k]) == 0):
                tempList.append(arr[i])
                tempList.append(arr[j])
                tempList.append(arr[k])
                ansList.append(tempList)
        tempList = []
print(ansList)
 
# 8
# Enter array: -25 -10 -7 -3 2 4 8 10
# [[-10, 2, 8], [-7, -3, 10]]

# Ans9
def areBracketsBalanced(expr):
    stack = []
    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    if stack:
        return False
    return True
if __name__ == "__main__":
    expr = input()
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")
 
# ({[]})
# Balanced
# ([{]) 
# Not Balanced






