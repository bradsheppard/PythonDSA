from typing import List


def merge_sort(array: List[int]):
    aux_array = list(array)
    _merge_sort_helper(array, aux_array, 0, len(array) - 1)


def _merge_sort_helper(array: List[int], aux_array: List[int], start: int, end: int):
    if start == end:
        return

    mid = (start + end) // 2
    _merge_sort_helper(aux_array, array, start, mid)
    _merge_sort_helper(aux_array, array, mid + 1, end)

    _do_merge(array, aux_array, start, mid, end)


def _do_merge(array: List[int], aux_array: List[int], start: int, mid: int, end: int):
    i = start
    j = mid + 1
    k = start

    while i <= mid and j <= end:
        if aux_array[i] <= aux_array[j]:
            array[k] = aux_array[i]
            k += 1
            i += 1
        else:
            array[k] = aux_array[j]
            k += 1
            j += 1

    while i <= mid:
        array[k] = aux_array[i]
        k += 1
        i += 1
    while j <= end:
        array[k] = aux_array[j]
        k += 1
        j += 1


def test_merge_sort():
    nums = [3, 8, 9, 1, -23, -78, 90, 100, 3]
    sorted_nums = list(nums)
    sorted_nums.sort()

    merge_sort(nums)

    assert nums == sorted_nums

