scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
h = max(scores)
i = scores.index(h)
print(h, i)

l = min(scores)
c = scores.count(l)
print(l, c)

r = list(scores[::-1])
print(r)

x = 76
if x in scores:
    print(scores.index(x))
else:
    print("Not present")
