# AIM: Find a subset of a given set S whose sum is equal to a given positive integer d.

subsets = [[]]  # List to store subsets
ans = []  # List to store subsets with the desired sum

def generate_subsets(res, list1):
    subsets.append(res)  # Append the current subset to the list
    if not list1:  # Base case: if the list is empty
        return
    for j in range(len(list1)):
        generate_subsets(res + [list1[j]], list1[j+1:])  # Recursive call with updated subset and remaining elements

arr = [1, 2, 5, 6, 8]  # Given set
n = 9  # Desired sum

# Generate all subsets using backtracking
for i in range(len(arr)):
    generate_subsets([arr[i]], arr[i+1:])

# Find subsets with the desired sum
for i in range(len(subsets)):
    if sum(subsets[i]) == n:
        ans.append(subsets[i])

# Output the subsets with the desired sum or a suitable message if no solution
if len(ans) == 0:
    print("There is no subset with the given sum")
else:
    for i in range(len(ans)):
        print(ans[i])

# Output:
# [1, 2, 6]
# [1, 8]
