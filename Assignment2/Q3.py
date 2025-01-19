import random

nums = []
for i in range(100):
    nums.append(random.randint(100, 900))

odds = []
evens = []
for n in nums:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

primes = []
for n in nums:
    if n > 1:
        for j in range(2, n):
            if n % j == 0:
                break
        else:
            primes.append(n)

print(odds)
print(evens)
print(primes)
