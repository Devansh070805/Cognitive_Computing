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