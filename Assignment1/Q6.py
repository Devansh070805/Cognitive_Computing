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