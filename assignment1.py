import random

# 1) Write an algorithm that finds the m smallest numbers in a list.
S = random.sample(range(0, 100), 20)
m = 4

print(f"Set S: {S}")

for i in range(m):
    min = i
    for j in range(i + 1, len(S)):
        if S[min] > S[j]:
            min = j
    S[i], S[min] = S[min], S[i]

print(f"{m} smallest numbers in S: {S[:m]}")

# 2) Write an algorithm that prints out all subsets of three elements of a set of n elements.
S = random.sample(range(0, 100), 5)
print(f"\nSet S: {S}")

for i in range(len(S) - 2):
    for j in range(i + 1, len(S) - 1):
        for k in range(j + 1, len(S)):
            print(f"({S[i]}, {S[j]}, {S[k]})")

# 3) Discuss and write the Insertion Sort algorithm.
S = random.sample(range(0, 100), 20)
print(f"\nSet S: {S}")

for i in range(1, len(S)):
    current_element = S[i]
    j = i - 1
    while j >= 0 and current_element < S[j]:
        S[j + 1] = S[j]
        j -= 1
    S[j + 1] = current_element

print(f"S after insertion sort {S}")

# 4) Write an algorithm to find the greatest common divisor of two integers.
# Implementing Euclidean algorithm
a = random.randint(1, 1000)
b = random.randint(1, 1000)

print(f"\na: {a}, b: {b}")

while b != 0:
    tmp = b
    b = a % b
    a = tmp

print(f"GCD is {a}")