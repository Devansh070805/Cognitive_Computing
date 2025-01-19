A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

u = A | B
print(u)

i = A & B
print(i)

s = A ^ B
print(s)

print(A.issubset(B))
print(B.issuperset(A))

x = (int)(input())
if x in A:
    A.remove(x)
    print(A)
else:
    print("Not present")
