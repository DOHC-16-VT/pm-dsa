"""
Jira: PMB-101
Title: Two Sum Using a Hash Map

Problem:
Find two distinct indices whose values sum to target.

Algorithm:
1. Create a dictionary to store previously seen values and indices.
2. For each value, calculate target - value.
3. If the complement exists, return both indices.
4. Otherwise, store the current value and its index.

Time Complexity: O(n) expected
Space Complexity: O(n)
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    raise ValueError("No valid solution exists")


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]

    print("PMB-101: All tests passed!")
