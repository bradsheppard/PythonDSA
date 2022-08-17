from typing import List, Optional


def binary_search(nums: List[float], target: float) -> Optional[int]:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        val = nums[mid]

        if target == val:
            return mid
        elif target > val:
            left = mid + 1
        else:
            right = mid - 1


def test_binary_search_existing_element():
    nums = [1, 4.1, 5, 6.4, 9, 10.4, 11.6, 12.5, 67.3]
    index = binary_search(nums, 12.5)

    assert index == 7


def test_binary_search_nonexisting_element():
    nums = [1, 4.1, 5, 6.4, 9, 10.4, 11.6, 12.5, 67.3]
    index = binary_search(nums, 11.5)

    assert index == None

