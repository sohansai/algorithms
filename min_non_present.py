# AIM: Given an array A of length N, find an integer Z strictly greater than X such that Z is not present in the array A.
# The objective is to minimize the value of Z.

# Program:

# Read input values for N (length of array A) and q (number of queries)
n, q = [int(i) for i in input().split()]

# Read input values for the array A
l = [int(i) for i in input().split()]

# Sort the array A in ascending order
l.sort()

# Create a dictionary to store the mapping of elements in A to the next greater element
d = {}

i = 0
while i < len(l):
    j = i
    # Find the consecutive elements in A that differ by more than 1
    for j in range(i, len(l) - 1):
        if l[j] < l[j+1] - 1:
            break

    # If the last two elements in A are consecutive, include the second element as well
    if j == len(l) - 2:
        if l[j] == l[j+1] - 1:
            j += 1

    # Map each element in the consecutive range to the next greater element
    for k in range(i, j+1):
        d[l[k]] = l[j]

    # Move the index to the next unprocessed element
    i = j + 1

# Process the queries
while q:
    x = int(input())

    # Check if x exists in the dictionary, if not, check if x+1 exists, and so on
    if d.get(x, 0) == 0:
        if d.get(x+1, 0) == 0:
            print(x+1)
        else:
            print(d[x+1] + 1)
    else:
        print(d[x] + 1)

    q -= 1
