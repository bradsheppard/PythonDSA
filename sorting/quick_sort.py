from typing import List


def quick_sort(nums: List[int]) -> List[int]:
    _quick_sort_helper(nums, 0, len(nums) - 1)
    return nums


def _quick_sort_helper(nums: List[int], start: int, end: int):
    if start >= end:
        return

    left = start + 1
    right = end
    pivot = start

    while left <= right:
        if nums[left] > nums[pivot] and nums[right] < nums[pivot]:
            _swap(nums, left, right)
        if nums[left] <= nums[pivot]:
            left += 1
        if nums[right] >= nums[pivot]:
            right -= 1

    _swap(nums, pivot, right)
    _quick_sort_helper(nums, start, right - 1)
    _quick_sort_helper(nums, right + 1, end)


def _swap(nums: List[int], pos1: int, pos2: int):
    temp = nums[pos1]
    nums[pos1] = nums[pos2]
    nums[pos2] = temp


def test_quick_sort():
    nums = [3, 8, 9, 1, -23, -78, 90, 100, 3]
    sorted_nums = list(nums)
    sorted_nums.sort()

    quick_sort(nums)

    assert nums == sorted_nums

