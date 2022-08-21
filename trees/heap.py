from typing import List


class MinHeap:

    def __init__(self, nums: List[float]) -> None:
        self.heap = self.build_heap(nums)

    def build_heap(self, nums: List[float]) -> List[float]:
        self.heap = []

        for num in nums:
            self.insert(num)

        return self.heap

    def peek(self):
        return self.heap[0]

    def insert(self, num: float):
        self.heap.append(num)
        self.sift_up()

    def remove(self):
        heap_end = self.heap.pop()

        if self.heap:
            heap_top = self.heap[0]
            self.heap[0] = heap_end
            self.sift_down()

            return heap_top

        return heap_end

    def sift_up(self):
        index = len(self.heap) - 1
        parent_index = (index - 1) // 2

        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.swap(index, parent_index)
            index = parent_index
            parent_index = (index - 1) // 2

    def sift_down(self):
        index = 0
        child1_index = 2 * index + 1
        end_index = len(self.heap) - 1

        while child1_index <= end_index:
            child2_index = 2 * index + 2

            val = self.heap[index]
            child1_val = self.heap[child1_index]
            child2_val = self.heap[child2_index] if child2_index <= end_index else float('inf')

            if child1_val < child2_val and child1_val < val:
                self.swap(child1_index, index)
                index = child1_index
                child1_index = 2 * index + 1
            elif child2_val < val:
                self.swap(child2_index, index)
                index = child2_index
                child1_index = 2 * index + 1
            else:
                return

    def swap(self, index1: int, index2: int):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp


def test_min_heap():
    heap = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
    heap.insert(76)

    assert heap.peek() == -5

    heap.remove()
    assert heap.peek() == 2

    heap.remove()
    assert heap.peek() == 6

    heap.remove()
    assert heap.peek() == 7

    heap.insert(-10)
    assert heap.peek() == -10
