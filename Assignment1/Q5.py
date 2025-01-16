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
