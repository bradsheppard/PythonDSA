from typing import List
from disjoint_set.disjoint_set import DisjointSet


def mst(n: int, connections: List[List[int]]) -> int:
    connections.sort(key=lambda x: x[2])

    disjoint_set = DisjointSet(n)

    total_cost = 0
    edges = 0

    for connection in connections:
        src, dest, cost = connection

        if disjoint_set.is_same_component(src, dest):
            continue

        disjoint_set.union(src, dest)

        total_cost += cost

        edges += 1

    if edges == n - 1:
        return total_cost

    return -1


def test_valid_mst():
    n = 3
    connections = [[0, 1, 5], [0, 2, 6], [1, 2, 1]]

    total_cost = mst(n, connections)

    assert total_cost == 6


def test_invalid_mst():
    n = 4
    connections = [[0, 1, 3], [2, 3, 4]]

    total_cost = mst(n, connections)

    assert total_cost == -1
