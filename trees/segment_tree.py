from typing import List


class Node:

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.val = 0
        self.left: Node | None = None
        self.right: Node | None = None


class SegmentTree:

    def __init__(self, nums: List[int]):

        def build_helper(nums: List[int], start: int, end: int):
            if start == end:
                node = Node(start, end)
                node.val = nums[start]
                return node

            mid = (start + end) // 2

            node = Node(start, end)

            node.left = build_helper(nums, start, mid)
            node.right = build_helper(nums, mid + 1, end)

            node.val = node.left.val + node.right.val

            return node

        self.root = build_helper(nums, 0, len(nums) - 1)


    def update(self, index: int, val: int):

        def update_helper(node, index: int, val: int):
            if node.start == node.end:
                node.val = val
                return

            mid = (node.start + node.end) // 2

            if index <= mid:
                update_helper(node.left, index, val)
            else:
                update_helper(node.right, index, val)

            node.val = node.left.val + node.right.val

        update_helper(self.root, index, val)


    def range_query(self, start: int, end: int) -> int:

        def query_helper(node, start: int, end: int) -> int:
            if node.start == start and node.end == end:
                return node.val

            mid = (node.start + node.end) // 2

            if end <= mid:
                return query_helper(node.left, start, end)
            elif start >= mid + 1:
                return query_helper(node.right, start, end)
            else:
                return query_helper(node.left, start, mid) + query_helper(node.right, mid + 1, end)

        return query_helper(self.root, start, end)


def test_segment_tree():
    nums = [1, 4, 7, 3, -2, 4, 23, 45, 2, 12]

    segment_tree = SegmentTree(nums)

    assert segment_tree.range_query(0, 2) == 12
    assert segment_tree.range_query(2, 5) == 12
    assert segment_tree.range_query(7, 8) == 47
    assert segment_tree.range_query(0, len(nums) - 1) == sum(nums)

    segment_tree.update(2, 1)
    segment_tree.update(0, 0)

    assert segment_tree.range_query(0, 2) == 5


