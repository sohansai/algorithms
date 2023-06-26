# AIM: Determine the minimum time required to send all groups from the source to the destination using the given planes with specific capacities.

n, m = map(int, input().split())  # Input: number of groups (n) and number of planes (m)
p = list(map(int, input().split()))  # Input: capacities of planes
a = list(map(int, input().split()))  # Input: sizes of groups

p.sort()  # Sort the plane capacities in ascending order
a.sort()  # Sort the group sizes in ascending order
p = p[::-1]  # Reverse the sorted plane capacities to get them in descending order
a = a[::-1]  # Reverse the sorted group sizes to get them in descending order

if a[0] < p[0]:
    print(-1)  # If the largest group size is smaller than the largest plane capacity, it is not possible to send all groups
else:
    i = 1
    mxt = 1  # Maximum time required
    j = 1
    time = 1

    while i < n:
        while a[j] < p[i]:
            time += 2
            i += 1
        mxt = max(mxt, time)
        time = 1
        j += 1
        i += 1

        if j > m-1:
            time = 2 * (((n - i) // m) + ((n - i) % m))
            mxt += time
            break

    print(mxt)  # Output: minimum time required to send all groups from source to destination

# Input: 4 3
#        2 1 2 6
#        5 5 6
# Output: 3
