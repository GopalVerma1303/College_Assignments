#Ans1:
def reverse_string(str):  
    str1 = ""  
    for i in str:  
        str1 = i + str1  
    return str1      
s = str(input("Enter the string: "))  
print("The original string is: ",s)  
print("The reverse string is: ",reverse_string(s))
 
#Ans2:
min = int(input("Enter min value: "))
max = int(input("Enter max value: "))
num = int(input("Enter the number: "))
for i in range(min, max):
    if(i%num==0):
        print(i)
 
#Ans3:
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(area)
 
#Ans4:
for i in range(6):
    for j in range(i):
        print("* ", end="")
    print()
for i in range(4, 0, -1):
    for j in range(i):
        print("* ", end="")
    print()
 
#Ans5: 
value = 65
for i in range(0, 5):
    for j in range(0, i+1):
        ch = chr(value)
        print(ch, end=" ")
        value = value + 1
    print()
 
#Ans6:
lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))   
print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  
 
#Ans7:
for i in range(1, 500):
    if(i%77==0):
        print(i)
 
#Ans8:
lst = []
for i in range(0, 10):
    ele = int(input())
    lst.append(ele) 
pn = []
nn = []
on = []
en = []
for i in range(0, 10):
    if(i>=0):
        pn.append(i)
    if(i<0):
        nn.append(i)
    if(i%2==0):
        on.append(i)
    if(i%2!=0):
        en.append(i)
print(pn)
print(nn)
print(on)
print(en)
def word_count(lst):
    counts = dict()
    for word in lst:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print( word_count(lst))
 
#Ans9:
def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
s = str(input())
print( word_count(s))
