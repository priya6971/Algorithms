# Application of Dynamic Programming - To find single source shortest path
# Implementation of Bellman Ford Algorithm
# Time Complexity : O(VE)
class Graph:
    def __init__(self, vertices):
        self.V = vertices   # Total number of vertices in the graph
        self.graph = []     # Array of edges

    # Add edges
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    # Print the solution
    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def bellman_ford(self, src):

        # Step 1: fill the distance array and predecessor array
        dist = [float("Inf")] * self.V
        # Mark the source vertex
        dist[src] = 0

        # Step 2: relax edges |V| - 1 times
        for i in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        # Step 3: detect negative cycle
        # if value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        # No negative weight cycle found!
        # Print the distance and predecessor array
        self.print_solution(dist)


g = Graph(8)
g.add_edge(1, 2, 6)
g.add_edge(1, 3, 5)
g.add_edge(1, 4, 5)
g.add_edge(2, 5, -1)
g.add_edge(3, 2, -2)
g.add_edge(3, 5, 1)
g.add_edge(4, 3, -2)
g.add_edge(4, 6, -1)
g.add_edge(5, 7, 3)
g.add_edge(6, 7, 3)

g.bellman_ford(1)