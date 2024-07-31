class DisjointSet:

    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.num_components = n

    ## Path Halving
    def find_root(self, x: int):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x

    # Path Compression
    def find_root_compress(self, x: int):
        root = x

        while self.parent[root] != root:
            root = self.parent[root]

        while self.parent[x] != root:
            parent = self.parent[x]
            self.parent[x] = root
            x = parent

        return root

    def is_same_component(self, x: int, y: int):
        x_root = self.find_root(x)
        y_root = self.find_root(y)

        return x_root == y_root

    def union(self, x: int, y: int):
        root_x = self.find_root(x)
        root_y = self.find_root(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_y] < self.rank[root_x]:
            self.parent[root_y] = root_x
        else:
            self.rank[root_y] += 1
            self.parent[root_x] = root_y

        self.num_components -= 1


def test_disjoint_set():
    disjoint_set = DisjointSet(7)
    disjoint_set.union(1, 2)
    disjoint_set.union(2, 3)

    assert disjoint_set.num_components == 5

    assert disjoint_set.find_root(1) == disjoint_set.find_root(3)
    assert disjoint_set.find_root(4) != disjoint_set.find_root(5)


def test_disjoint_set_path_compression():
    disjoint_set = DisjointSet(7)
    disjoint_set.union(1, 2)
    disjoint_set.union(2, 3)

    assert disjoint_set.num_components == 5

    assert disjoint_set.find_root_compress(1) == disjoint_set.find_root_compress(3)
    assert disjoint_set.find_root_compress(4) != disjoint_set.find_root_compress(5)
