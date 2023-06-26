# AIM: Find and display the good pairs of strings from a given table of binary strings.

# Function to find and display the good pairs of strings
def find_good_pairs():
    t = int(input())  # Number of test cases

    while t > 0:
        t -= 1
        n = int(input())  # Number of binary strings in the table

        same = [0, 0]  # Count of strings with no '0' and no '1' respectively

        for i in range(n):
            s = input()  # Binary string
            if s.find('0') == -1:
                same[1] += 1
            elif s.find('1') == -1:
                same[0] += 1

        # Calculate and output the count of good pairs of strings
        print(n * (n - 1) // 2 - same[0] * same[1])


# Input
# Example: 1 (Number of test cases)
#          5 (Number of binary strings)
#          00
#          1111
#          0001
#          11
#          01
t = int(input())  # Number of test cases

while t > 0:
    t -= 1
    n = int(input())  # Number of binary strings in the table

    same = [0, 0]  # Count of strings with no '0' and no '1' respectively

    for i in range(n):
        s = input()  # Binary string
        if s.find('0') == -1:
            same[1] += 1
        elif s.find('1') == -1:
            same[0] += 1

    # Calculate and output the count of good pairs of strings
    print(n * (n - 1) // 2 - same[0] * same[1])
