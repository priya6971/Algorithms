# Implementation of Floyd's Warshall Algorithm
number_of_vertices = 4
# Randomly defining high number as Infinite value
INF = 999

# Method to print the solution
def print_sol(distance):
    for i in range(number_of_vertices):
        for j in range(number_of_vertices):
            if (distance[i] [j] == INF):
                print("Inf", end = " ")
            else:
                print(distance[i][j], end = " ")
        print(" ")

# Algorithm Implementation of Floyd's Warshall
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))
    # Adding vertices individually
    for k in range(number_of_vertices):
        # Generating Matrix
        for i in range(number_of_vertices):
            for j in range(number_of_vertices):
                distance[i] [j] = min(distance[i] [j], distance[i] [k] + distance[k] [j])
    print_sol(distance)

# Graph Initialization
G = [[0, 3, INF, 7],
     [8, 0, 2, INF],
     [5, INF, 0, 1],
     [2, INF, INF, 0]]

floyd_warshall(G)
