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
"""
Insertion Sort is a sorting algorithm that builds the sorted array one element at a time.
It maintains a sorted and unsorted parts of the array. It can be implemented by using
two loops. It takes out the current element and then uses the inner loop to find the correct
position of that element and move the other elements by one position to make space for it.
The worst case time complexity is O(n^2).
"""
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
# I did some research and decided to implement the Euclidean algorithm
# https://en.wikipedia.org/wiki/Greatest_common_divisor#Euclidean_algorithm
a = random.randint(1, 1000)
b = random.randint(1, 1000)

print(f"\na: {a}, b: {b}")

while b != 0:
    tmp = b
    b = a % b
    a = tmp

print(f"GCD is {a}")
