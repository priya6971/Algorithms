import heapq

#Dijkstra's Algorithm
def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            ## Relaxation of Edges
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


distances = {
    'A': {'B': 50, 'C': 100},
    'B': {'C': 150, 'D': 3},
    'C': {'B': -80, 'D': 7},
    'D': {}
}
print(calculate_distances(distances, 'A'))