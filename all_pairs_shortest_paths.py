# AIM: Implement the All Pairs Shortest Paths problem using the Floyd-Warshall algorithm.

nV = 4  # Number of vertices
INF = 999  # Infinite value

def floyd_warshall(graph):
    distance = list(map(lambda i: list(map(lambda j: j, i)), graph))  # Create a copy of the graph
    
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    print_solution(distance)

def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end=" ")
        print()

# Input
graph = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]

# Call the Floyd-Warshall algorithm
floyd_warshall(graph)

# Output
# Example:
# 0 3 7 5
# 2 0 6 4
# 3 1 0 5
# 5 3 2 0
