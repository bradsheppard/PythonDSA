from typing import List


def quick_select(array: List[int], k: int):
    position = k - 1
    return quick_select_helper(array, 0, len(array) - 1, position)


def quick_select_helper(array: List[int], start: int, end: int, position: int) -> int:
    while True:

        if start > end:
            raise Exception('Not found')

        left = start + 1
        right = end
        pivot = start

        while left <= right:

            if array[left] > array[pivot] and array[right] < array[pivot]:
                swap(array, left, right)
            if array[left] <= array[pivot]:
                left += 1
            if array[right] >= array[pivot]:
                right -= 1

        swap(array, right, pivot)

        if right == position:
            return array[right]
        elif right < position:
            start = right + 1
        else:
            end = right - 1


def swap(array: List[int], i: int, j: int):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def test_quick_sort():
    nums = [4, 8, 9, 1, -23, -78, 90, 100, 3]
    sorted_nums = list(nums)
    sorted_nums.sort()

    result = quick_select(nums, 2)

    assert result == -23

