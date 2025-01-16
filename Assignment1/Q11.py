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
