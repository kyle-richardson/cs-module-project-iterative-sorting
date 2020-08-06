from iterative_sorting import bubble_sort
import math


def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # sort first
    sortedArr = bubble_sort(arr)
    low = 0
    high = len(sortedArr) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == sortedArr[mid]:
            return mid
        elif target < sortedArr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1  # not found
