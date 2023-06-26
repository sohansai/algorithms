# AIM: Given the marks and bounds of students in a class, find the maximum number of students that can pass if arranged properly.

# Function to calculate the maximum number of students that can pass
def maximum_students_pass(t):
    while t:
        n = int(input())  # Number of students

        students = []  # List to store the marks and bounds of students
        for _ in range(n):
            l = [int(i) for i in input().split()]  # Input marks and bounds of each student
            students.append(l)

        students.sort(key=lambda x: x[0] + x[1])  # Sort students based on marks + bounds

        dp = [0] + [int(1e18)] * n  # Initialize dynamic programming array

        # Calculate the maximum number of students that can pass
        for s in students:
            for j in range(n, 0, -1):
                if s[0] >= dp[j - 1]:
                    dp[j] = min(dp[j], dp[j - 1] + s[1])

        max_pass = n - dp.count(int(1e18))  # Calculate the maximum number of students that passed
        print(max_pass)  # Output the result

        t -= 1


# Input
t = int(input())  # Number of test cases

# Call the function to find the maximum number of students that can pass
maximum_students_pass(t)
