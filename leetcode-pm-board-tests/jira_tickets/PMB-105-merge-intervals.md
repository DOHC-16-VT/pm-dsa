# PMB-105 — Merge Overlapping Intervals Using Sorting

**Issue Type:** Story
**Priority:** Medium
**Expected GitHub file:** `solutions/PMB-105-merge-intervals.py`
**Suggested branch:** `feature/PMB-105-merge-intervals`

## Description

As a developer, I want to merge overlapping intervals into non-overlapping
intervals, so that I can simplify collections of time ranges or numerical
ranges.

## Problem Statement

Given an array of intervals where each interval is represented as
`[start, end]`, merge all overlapping intervals and return an array of the
resulting non-overlapping intervals.

The resulting intervals must be sorted by their start values.

Two intervals that share an endpoint are considered overlapping.

### Examples

Input:
`intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]`

Output:
`[[1, 6], [8, 10], [15, 18]]`

Explanation: The intervals `[1, 3]` and `[2, 6]` overlap, so they are
merged into `[1, 6]`.

Additional examples:

- `[[1, 4], [4, 5]]` → `[[1, 5]]`
- `[[1, 4], [0, 2], [3, 5]]` → `[[0, 5]]`
- `[[1, 2]]` → `[[1, 2]]`
- `[]` → `[]`

## Functional Requirements

1. Accept a list of intervals.
2. Sort intervals by their starting values.
3. Merge overlapping intervals.
4. Return the merged intervals in ascending order.
5. Handle empty input and intervals that share endpoints.
6. Implement the solution in Python.

## Acceptance Criteria

- [ ] Correctly merges overlapping intervals.
- [ ] Preserves non-overlapping intervals.
- [ ] Merges intervals sharing an endpoint.
- [ ] Returns an empty list for empty input.
- [ ] Returns intervals in sorted order.
- [ ] Achieves O(n log n) time complexity.
- [ ] Uses O(n) auxiliary space for the result in the general case.
- [ ] The implementation is available in GitHub and linked to PMB-105.

## Definition of Done

The solution passes all acceptance tests, includes complexity analysis and
documentation, and is associated with the correct Jira issue through the
PM Board.
