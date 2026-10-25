"""
Jira: PMB-104
Title: Maximum Subarray Using Kadane's Algorithm

Algorithm:
1. Initialize current_sum and max_sum to the first element.
2. For every subsequent element, decide whether to:
   a. Extend the current subarray, or
   b. Start a new subarray.
3. Update the maximum sum whenever a better sum is found.
4. Return max_sum.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def max_subarray(nums: list[int]) -> int:
    if not nums:
        raise ValueError("Input array must not be empty")

    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    assert max_subarray(
        [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ) == 6

    assert max_subarray([1]) == 1
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    assert max_subarray([-3, -2, -5]) == -2
    assert max_subarray([-1, -2]) == -1

    print("PMB-104: All tests passed!")
