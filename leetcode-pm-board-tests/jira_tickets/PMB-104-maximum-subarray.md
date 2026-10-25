# PMB-104 — Find the Maximum Subarray Sum Using Kadane's Algorithm

**Issue Type:** Story
**Priority:** High
**Expected GitHub file:** `solutions/PMB-104-maximum-subarray.py`
**Suggested branch:** `feature/PMB-104-maximum-subarray`

## Description

As a developer, I want to find the contiguous subarray with the largest
sum, so that I can efficiently identify the most valuable consecutive
segment in a sequence of integers.

## Problem Statement

Given an integer array `nums`, find the contiguous, non-empty subarray with
the largest sum and return that sum.

### Examples

- Input: `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]` → Output: `6`
- Input: `nums = [1]` → Output: `1`
- Input: `nums = [5, 4, -1, 7, 8]` → Output: `23`
- Input: `nums = [-3, -2, -5]` → Output: `-2`

## Functional Requirements

1. Accept a non-empty array of integers.
2. Return the maximum sum of any contiguous, non-empty subarray.
3. Handle positive, negative, and mixed integer values.
4. Implement Kadane's algorithm.
5. Achieve linear time complexity.

## Acceptance Criteria

- [ ] Returns `6` for the first example.
- [ ] Returns `1` for a single-element positive array.
- [ ] Returns `23` for `[5, 4, -1, 7, 8]`.
- [ ] Correctly handles arrays containing only negative numbers.
- [ ] Never assumes that the maximum sum must be positive.
- [ ] Achieves O(n) time complexity.
- [ ] Uses O(1) auxiliary space.
- [ ] The GitHub implementation is linked to PMB-104.

## Definition of Done

All acceptance criteria pass. The Python solution, algorithm explanation,
complexity analysis, and tests are available in GitHub and associated with
the correct Jira ticket.
