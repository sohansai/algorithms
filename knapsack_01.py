# AIM: Implement the 0/1 Knapsack problem using the Dynamic Programming method.

# Function to solve the 0/1 Knapsack problem
def knapsack_01():
    n, c = [int(i) for i in input().split()]  # Number of items and the maximum capacity of the knapsack
    v = [int(i) for i in input().split()]  # List of item values
    w = [int(i) for i in input().split()]  # List of item weights

    dp = [[0] * (c + 1) for _ in range(n + 1)]  # Dynamic programming array

    # Dynamic programming approach to solve the knapsack problem
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            dp[i][j] = dp[i - 1][j]
            if w[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], v[i - 1] + dp[i - 1][j - w[i - 1]])

    print(dp[-1][-1])  # Output the maximum value of items that can be packed in the knapsack


# Input
# Format: [Number of items] [Maximum capacity]
#         [List of item values]
#         [List of item weights]
# Example: 4 10
#          10 40 30 50
#          5 4 6 3
n, c = [int(i) for i in input().split()]  # Number of items and the maximum capacity of the knapsack
v = [int(i) for i in input().split()]  # List of item values
w = [int(i) for i in input().split()]  # List of item weights

dp = [[0] * (c + 1) for i in range(n + 1)]  # Dynamic programming array

# Dynamic programming approach to solve the knapsack problem
for i in range(1, n + 1):
    for j in range(1, c + 1):
        dp[i][j] = dp[i - 1][j]
        if w[i - 1] <= j:
            dp[i][j] = max(dp[i - 1][j], v[i - 1] + dp[i - 1][j - w[i - 1]])

print(dp[-1][-1])  # Output the maximum value of items that can be packed in the knapsack
