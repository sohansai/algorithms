# AIM: Find beautiful numbers in the given interval from M to N, where a beautiful number has 2N digits and the sum of the first N digits is equal to the sum of the last N digits.

l, m = [int(i) for i in input().split()]  # Input: range from l to m
res = []  # List to store beautiful numbers

for i in range(l, m+1):
    s = str(i)  # Convert the number to string
    if len(s) % 2 != 0:  # Skip if the number of digits is odd
        continue
    p1 = 0
    p = 0
    for j in range(len(s)):
        if j < len(s) // 2:
            p1 += int(s[j])  # Sum of the first N digits
        p += int(s[j])  # Sum of all digits
    if p1 == (p - p1):  # Check if the sums are equal
        res.append(s)  # Add the beautiful number to the list

# Output the beautiful numbers or a suitable message if none exists
if len(res) == 0:
    print("There is no beautiful number")
else:
    for i in range(len(res)):
        print(res[i])

# Input: 10 30
# Output:
# 11
# 22
