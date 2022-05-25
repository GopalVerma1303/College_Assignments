#Ans1:
grade = int(input("Enter grade: "))
if(grade < 25): print('F')
elif(grade in range(25, 45)): print('E')
elif(grade in range(45, 50)): print('D')
elif(grade in range(50, 60)): print('C')
elif(grade in range(60, 80)): print('B')
else: print('A')

#Ans2:
def is_leap(year):
    leap = False
    if year%400==0:
        leap= True
    elif year%4==0 and year%100!=0:
        leap=True
    return leap
year = int(input())
print(is_leap(year))

#Ans3:
import random
for i in range(1, 11):
    a = random.randint(0,10)
    b = random.randint(0,10)
    qstr = "Question " +str(i)+ ": " +str(a)+ " X " +str(b)+ " = "
    ans = int(input(qstr))
    if(ans != a*b):
        print("Wrong. The answer is "+str(a*b))
    else:
        print("Right!")

#Ans4:
for candies in range(200):
    if (candies % 5 != 2):
        continue
    if (candies % 6 != 3):
        continue
    if (candies % 7 != 2):
        continue
    print("There are a total " + str(candies) + " pieces in the bowl.")
    break