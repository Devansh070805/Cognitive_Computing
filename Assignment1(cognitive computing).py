#Question 1:
print("Hello World")

#Question 2:

#2.1
a,b=3,5
print(a+b)

#2.2
str1="Hey"
str2= "There!"
#print(str1+str2)-> this will throw an error
print(str1,str2)

#2.3
print(str1,a)

#Question 3:

#3.1
num=(int)(input("Enter a Number: "))
if num==0:
    print("The number is Zero")
elif num<0:
    print("The number is negative")
else:
    print("The number is positive")
 
#3.2
if num%2==0:
    print(num, "is even")
else:
    print(num,"is odd")

#Question 4:

#4.1
for i in range (1,11):
    print(i)

#4.2
i=1
while i<=10:
    print(i)
    i+=1

#4.3
sum=0
for i in range (1,101):
    sum+=i

print("Sum= ",sum)

#Question 5:

#5.1
myList=[1,2,3,4,5]
min=max=myList[0]
for item in myList:
    if item>max:
        max=item
    elif item<min:
        min=item
print("Minimum value in the List: ",min)
print("Maximum value in the List: ",max)

#5.2
myDict={
    1:"One",
    2:"Two",
    3:"Three"
}
print(myDict)
print(myDict[1])

#5.3

#using inbuilt functions:
myList.sort()
print(myList) #ascending order
myList.sort(reverse=True)
print(myList) #descending order

#using loop implementation
n=len(myList)
for i in range(n):
    for j in range(n-1-i):
        if myList[j]>myList[j+1]:
            myList[j],myList[j+1]=myList[j+1],myList[j]  #ascending order
           


print(myList)

for i in range(n):
    for j in range(n-1-i):
        if myList[j]<myList[j+1]:
            myList[j],myList[j+1]=myList[j+1],myList[j]  #descending order
           


print(myList)

#5.4
newMyDict={
    4:"four",
    5:"five",
    6:"six"
}
mergedDict=myDict.copy()
for key,value in newMyDict.items():
    mergedDict[key]=value

print(mergedDict)


#Question 6:

#6.1
ss=(str)(input("Enter a String: "))
vowels="aeiouAEIOU"
count=0
for ch in ss:
    if vowels.find(ch)>=0:
        count+=1

print(f"Number of vowels in {ss} are: {count}")

#6.2
print(f"Original String: {ss}")
ss=ss[::-1]#negative step size
print(f"Reversed String: {ss}")


#6.3
flag=0
for i in range(len(ss)//2):
    if(ss[i]!=ss[len(ss)-1-i]):
        flag=1
        break

if flag==1:
    print(f"{ss} is Not a Palindrome")
else:
    print(f"{ss} is a Palindrome")

#Question 7:

#7.1
with open("example.txt", "w") as file:
    file.write("This is the first line.\nThis is the second line.")

with open("example.txt", "r") as file:
    content = file.read()

print("Content of the file:")
print(content)


#7.2
with open("example.txt", "a") as file:
    file.write("\nThis is an appended line.")

with open("example.txt", "r") as file:
    updated_content = file.read()

print("Updated content of the file:")
print(updated_content)


#7.3
with open("example.txt", "r") as file:
    lines = file.readlines()
    line_count = len(lines)

print(f"The number of lines in the file is: {line_count}")


#Question 8:

#8.1, #8.2, #8.3

try:
    dd=(int)(input("Enter a number to divide: "))
    mm=5
    result=mm/dd
    print(result)
except ZeroDivisionError:
    print("Invalid Division by zero")
except ValueError:
    print( "Input a Number!!! ")
finally:
    print("Execution Done")

#Question 9:

import random

#9.1
print("Printing five random numbers: ")
for i in range(5):
    randomInt=random.randint(1,100)
    print(randomInt)

#9.2
toCheckNum=random.randint(1,100)
print(f"{toCheckNum} is generated randomly to check for prime")
def checkPrime(num):
    cc=0
    for i in range(1,num):
        if num%i==0:
            cc+=1
    
    if cc==1:
        return True
    else: 
        return False

if checkPrime(toCheckNum):
    print(f"{toCheckNum} is a Prime Number")
else:
     print(f"{toCheckNum} is not a Prime Number")


#9.3
while True:
    choice=input("+ to roll again, . to stop ")
    if(choice=='.'):
        break
    gg=random.randint(1,6)
    print(f"Rolling Dice..., Got a {gg}")

#9.4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(numbers)

print("Shuffled list:", numbers)

#9.5
items = ["apple", "banana", "cherry", "date", "elderberry"]
selected_item = random.choice(items)

print("Randomly selected item:", selected_item)

#9.6
import string

def generate_password(length):
    chara=string.ascii_letters + string.digits + string.punctuation
    ans=''
    for i in range (length):
        ans+=random.choice(chara)
    return (ans)
 
print("Your generated Password:",generate_password(12))


#9.7
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
random_suit=random.choice(suits)
random_rank=random.choice(ranks)
print(f"Random Card is: {random_rank} of {random_suit}")


#Question 10:

import sys

#10.1
print(float(sys.argv[1]) + float(sys.argv[2]))

#10.2
print(len(sys.argv[1]))

#Question 11:

#11.1
import math

number = float(input("Enter a number: "))
square_root = math.sqrt(number)
print("The square root of", number, "is", square_root)


#11.2
from datetime import datetime

current_datetime = datetime.now()
print("Current date and time:", current_datetime)


#11.3

import os

files = os.listdir(".")
print("Files in the current directory:")
for file in files:
    print(file)

