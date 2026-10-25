# PMB-103 — Find a Target in a Sorted Array Using Binary Search

**Issue Type:** Story
**Priority:** High
**Expected GitHub file:** `solutions/PMB-103-binary-search.py`
**Suggested branch:** `feature/PMB-103-binary-search`

## Description

As a developer, I want to find a target value in a sorted integer array
efficiently, so that I can retrieve the target's index without scanning
every element.

## Problem Statement

Given a sorted array of distinct integers `nums` and an integer `target`,
return the index of the target if it exists. Otherwise, return `-1`.

The implementation must use binary search.

### Examples

- Input: `nums = [-1, 0, 3, 5, 9, 12]`, `target = 9` → Output: `4`
- Input: `nums = [-1, 0, 3, 5, 9, 12]`, `target = 2` → Output: `-1`
- Input: `nums = [5]`, `target = 5` → Output: `0`

## Functional Requirements

1. Accept a sorted array of distinct integers and a target.
2. Return the target's zero-based index when found.
3. Return `-1` when the target is absent.
4. Use an iterative binary search implementation.
5. Do not modify the input array.

## Acceptance Criteria

- [ ] Returns index `4` for the first example.
- [ ] Returns `-1` when the target does not exist.
- [ ] Correctly handles a single-element array.
- [ ] Correctly handles an empty array.
- [ ] Uses binary search rather than a linear scan.
- [ ] Achieves O(log n) time complexity.
- [ ] Uses O(1) auxiliary space.
- [ ] The solution is linked to Jira issue PMB-103 in GitHub.

## Definition of Done

The solution passes all test cases, includes complexity analysis, and is
correctly linked to the Jira issue through the PM Board.
