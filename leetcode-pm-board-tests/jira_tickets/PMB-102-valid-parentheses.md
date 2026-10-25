# PMB-102 — Validate Parentheses Using a Stack

**Issue Type:** Story
**Priority:** Medium
**Expected GitHub file:** `solutions/PMB-102-valid-parentheses.py`
**Suggested branch:** `feature/PMB-102-valid-parentheses`

## Description

As a developer, I want to validate whether a string containing parentheses
and brackets is correctly balanced, so that I can verify the structural
correctness of expressions.

## Problem Statement

Given a string `s` containing only `()`, `{}`, and `[]`, determine whether
the brackets are valid.

A string is valid when every opening bracket has a corresponding closing
bracket of the same type, and brackets close in the correct order.

### Examples

- Input: `s = "()"` → Output: `True`
- Input: `s = "()[]{}"` → Output: `True`
- Input: `s = "(]"` → Output: `False`
- Input: `s = "([)]"` → Output: `False`
- Input: `s = "{[]}"` → Output: `True`

## Functional Requirements

1. Accept a string containing the three supported bracket types.
2. Validate matching bracket types.
3. Validate the order in which brackets are closed.
4. Return a Boolean result.
5. Implement the solution using a stack in Python.

## Acceptance Criteria

- [ ] Correctly validates `()`, `()[]{}`, and `{[]}`.
- [ ] Rejects `(]`, `([)]`, and `((`.
- [ ] Rejects a closing bracket without a corresponding opening bracket.
- [ ] Returns `True` for an empty string.
- [ ] Uses a stack-based approach.
- [ ] Achieves O(n) time complexity.
- [ ] The corresponding GitHub solution is linked to PMB-102.
- [ ] The linked solution contains documentation and executable test cases.

## Definition of Done

All acceptance criteria pass, the implementation is committed to GitHub,
and the PM Board associates the solution with the correct Jira issue.
