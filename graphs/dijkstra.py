import collections
import heapq
from typing import List

def dijkstra(matrix: List[List[int]], k: int):
    edge_dict = collections.defaultdict(list)
    n = len(matrix)

    for edge in matrix:
        source, dest, weight = edge
        edge_dict[source].append((dest, weight))

    dist = [float('inf')] * n
    dist[k] = 0

    seen = set()
    heap = heapq.heapify([(0, k)])

    while heap:
        current_dist, source = heapq.heappop(heap)

        if current_dist == float('inf'):
            break

        if source in seen:
            continue

        seen.add(source)

        edges = edge_dict[source]

        for edge in edges:
            dest, weight = edge

            if dist[source] + weight < dist[dest]:
                dist[dest] = dist[source] + weight
                heapq.heappush(heap, (dist[dest], dest))

    return dist
