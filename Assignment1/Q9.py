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