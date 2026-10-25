"""
Jira: PMB-105
Title: Merge Overlapping Intervals

Algorithm:
1. Return an empty list if no intervals are provided.
2. Sort intervals by their starting points.
3. Initialize the result with the first interval.
4. For each remaining interval:
   - If it overlaps the last result interval, merge them.
   - Otherwise, append it as a new interval.
5. Return the merged intervals.

Time Complexity: O(n log n)
Space Complexity: O(n) auxiliary space for the result.
"""


def merge_intervals(
    intervals: list[list[int]]
) -> list[list[int]]:
    if not intervals:
        return []

    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0][:]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged


if __name__ == "__main__":
    assert merge_intervals(
        [[1, 3], [2, 6], [8, 10], [15, 18]]
    ) == [[1, 6], [8, 10], [15, 18]]

    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge_intervals(
        [[1, 4], [0, 2], [3, 5]]
    ) == [[0, 5]]

    assert merge_intervals([[1, 2]]) == [[1, 2]]
    assert merge_intervals([]) == []

    print("PMB-105: All tests passed!")
