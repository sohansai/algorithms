# AIM: Sort a given set of n integer elements using the merge sort method and compute its time complexities.
#      Run the programs for varied values of n > 1000 and record the time taken to sort.
#      Plot a graph of the time taken versus n.
#      Demonstrate how the divide and conquer method works along with its time complexity analysis: worst case, average case, and best case.

import random
import math

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

print("Enter the number of graph values:")
val = int(input())

for _ in range(val):
    n = 1000 + random.randrange(1000)
    l = [random.randrange(-1000, 1000) for _ in range(n)]
    mergeSort(l)
    tc = n * (math.log(n))
    print("For the value", n, "the best, average, and worst time complexity is", tc)

# Output:
# Enter the number of graph values:
# 2
# For the value 1275 the best, average, and worst time complexity is 9117.14435843047
# For the value 1864 the best, average, and worst time complexity is 14036.81471113768
