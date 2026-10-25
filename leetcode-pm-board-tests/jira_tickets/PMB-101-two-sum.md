# PMB-101 — Implement Two Sum Using a Hash Map

**Issue Type:** Story
**Priority:** Medium
**Expected GitHub file:** `solutions/PMB-101-two-sum.py`
**Suggested branch:** `feature/PMB-101-two-sum`

## Description

As a developer, I want to identify two elements in an integer array whose sum
equals a specified target, so that I can efficiently determine the indices
of the required elements.

## Problem Statement

Given an integer array `nums` and an integer `target`, return the indices of
two distinct elements whose sum equals `target`.

Assume that exactly one valid solution exists. The same array element cannot
be used twice.

### Example

Input:
- `nums = [2, 7, 11, 15]`
- `target = 9`

Output:
- `[0, 1]`

Explanation: The elements at indices 0 and 1 add up to 9.

## Functional Requirements

1. Accept an integer array and an integer target.
2. Return the indices of two elements that sum to the target.
3. Do not use the same element twice.
4. Return the answer in O(n) expected time.
5. Implement the solution in Python.

## Acceptance Criteria

- [ ] The solution returns `[0, 1]` for `[2, 7, 11, 15]` with target `9`.
- [ ] The solution returns `[1, 2]` for `[3, 2, 4]` with target `6`.
- [ ] The solution returns `[0, 1]` for `[3, 3]` with target `6`.
- [ ] The implementation does not reuse the same index.
- [ ] The expected time complexity is O(n).
- [ ] The GitHub solution file is linked to this Jira ticket.
- [ ] The linked file contains the implementation, explanation, complexity
      analysis, and test cases.

## Definition of Done

The Python implementation is committed to GitHub, reviewed against the
acceptance criteria, and correctly associated with this Jira issue through
the PM Board.
