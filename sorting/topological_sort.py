from typing import List, Optional, Set


class Node:

    def __init__(self, val: str):
        self.val = val
        self.prereqs = []


class Graph:

    def __init__(self, letters: Set[str]):
        self.dict = {}
        
        for letter in letters:
            node = Node(letter)
            self.dict[letter] = node

    def add_prereq(self, letter: str, prereq: str):
        letter_node = self.dict[letter]
        prereq_node = self.dict[prereq]

        letter_node.prereqs.append(prereq_node)

    def get_total_ordering(self) -> Optional[List[str]]:
        result = []
        visited = set()
        visiting = set()

        def dfs(node: Node) -> bool:
            if node.val in visited:
                return False

            if node.val in visiting:
                return True

            visiting.add(node.val)

            for prereq in node.prereqs:
                has_cycle = dfs(prereq)

                if has_cycle:
                    return True

            visited.add(node.val)
            visiting.remove(node.val)

            result.append(node.val)

            return False
            

        for node in self.dict.values():
            if node.val in visited:
                continue

            has_cycle = dfs(node)

            if has_cycle:
                return None

        return result


def test_topological_sort_with_valid_order():
    nodes = ['1', '2', '3', '4']
    relations = [('1', '2'), ('1', '3'), ('3', '2'), ('4', '2'), ('4', '3')]

    graph = Graph(set(nodes))

    for relation in relations:
        graph.add_prereq(relation[1], relation[0])

    expected_total_ordering_1 = ['1', '4', '3', '2']
    expected_total_ordering_2 = ['4', '1', '3', '2']

    actual_total_ordering = graph.get_total_ordering()

    assert (actual_total_ordering == expected_total_ordering_1) or (actual_total_ordering == expected_total_ordering_2)


def test_topological_sort_without_valid_order():
    nodes = ['1', '2', '3', '4', '5', '6', '7', '8']
    relations = [
        ('3', '1'),
        ('8', '1'),
        ('8', '7'),
        ('5', '7'),
        ('5', '2'),
        ('1', '4'),
        ('6', '7'),
        ('1', '2'),
        ('7', '6')
    ]

    graph = Graph(set(nodes))

    for relation in relations:
        graph.add_prereq(relation[1], relation[0])

    expected_total_ordering = None
    actual_total_ordering = graph.get_total_ordering()

    assert actual_total_ordering == expected_total_ordering

