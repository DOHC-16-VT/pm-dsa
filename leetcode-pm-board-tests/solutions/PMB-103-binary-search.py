"""
Jira: PMB-103
Title: Binary Search

Algorithm:
1. Initialize left and right pointers.
2. Calculate the middle index.
3. If the middle element equals the target, return its index.
4. If the middle element is smaller, search the right half.
5. Otherwise, search the left half.
6. Return -1 if the target is absent.

Time Complexity: O(log n)
Space Complexity: O(1)
"""


def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([], 5) == -1
    assert binary_search([1, 3, 5, 7], 1) == 0
    assert binary_search([1, 3, 5, 7], 7) == 3

    print("PMB-103: All tests passed!")
