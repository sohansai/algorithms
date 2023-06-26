# AIM: You are given an array of integers A, and you need to find the maximum sum that can be obtained by picking 
# some non-empty subset of the array. If there are many such non-empty subsets, choose the one with the maximum 
# number of elements. Print the maximum sum and the number of elements in the chosen subset.

# Input
n = int(input("Enter the number of elements: ")) 
l = [int(i) for i in input("Enter the elements: ").split()]

# Initializing variables
s = 0   # current sum
k = 0   # count of elements in the chosen subset
m = l[0]   # maximum element

# Finding the maximum sum and the number of elements
for i in range(len(l)):
    if l[i] >= 0:
        s = s + l[i]
        k = k + 1

# Output
if s > 0:
    print("Maximum Sum:", s)
    print("Number of Elements in Subset:", k)
elif s == 0:
    for i in range(1, len(l)):
        if l[i] > m:
            m = l[i]
    print("Maximum Sum:", m)
    print("Number of Elements in Subset: 1")
