# Testing the PM Board End-to-End

This repo is a fixture for testing whether your **PM Board** correctly
bridges Jira tickets and their corresponding GitHub code solutions.

## Jira ↔ GitHub mapping

| Jira ID | Summary            | Algorithm           | Expected GitHub file              |
| ------- | ------------------- | -------------------- | ---------------------------------- |
| PMB-101 | Two Sum              | Hash map             | `solutions/PMB-101-two-sum.py`           |
| PMB-102 | Valid Parentheses    | Stack                | `solutions/PMB-102-valid-parentheses.py` |
| PMB-103 | Binary Search         | Binary search         | `solutions/PMB-103-binary-search.py`     |
| PMB-104 | Maximum Subarray      | Kadane's algorithm    | `solutions/PMB-104-maximum-subarray.py`  |
| PMB-105 | Merge Intervals       | Sorting               | `solutions/PMB-105-merge-intervals.py`   |

**Important:** The IDs above are proposed identifiers. Create the tickets in
your real Jira project and swap in the actual issue keys if Jira generates
different ones. For the strongest integration test, put the exact Jira
issue key in the GitHub filename, branch name, commit message, and PR
description — that gives the PM Board multiple chances to establish the
correct relationship.

## Suggested branch names

| Jira ticket | Branch name                         | File                                |
| ----------- | ------------------------------------ | ------------------------------------ |
| PMB-101     | `feature/PMB-101-two-sum`             | `PMB-101-two-sum.py`                 |
| PMB-102     | `feature/PMB-102-valid-parentheses`   | `PMB-102-valid-parentheses.py`       |
| PMB-103     | `feature/PMB-103-binary-search`       | `PMB-103-binary-search.py`           |
| PMB-104     | `feature/PMB-104-maximum-subarray`    | `PMB-104-maximum-subarray.py`        |
| PMB-105     | `feature/PMB-105-merge-intervals`     | `PMB-105-merge-intervals.py`         |

## Phase 1: Create Jira tickets

Create all five stories in your Jira project using the content in
`jira_tickets/`. For each ticket, verify:

- Summary is correct.
- Description contains the problem statement.
- Acceptance criteria are present.
- Issue key is unique.
- Status is initially `To Do`.

## Phase 2: Push solutions to GitHub

The five Python files are already in `solutions/`. Run each one (or the
pytest suite in `tests/test_solutions.py`) to verify tests pass before
pushing:

```bash
python solutions/PMB-101-two-sum.py
pytest tests/test_solutions.py -v
```

## Phase 3: Verify the Jira–GitHub connection

| Test ID | What to verify                      | Expected result                                               |
| ------- | ------------------------------------ | --------------------------------------------------------------- |
| TC-01   | Jira ticket exists                   | All five stories are available                                  |
| TC-02   | GitHub repository is connected       | Repository is accessible to the integration                     |
| TC-03   | Jira issue key is detected           | Correct issue key is identified                                 |
| TC-04   | Code is linked to the ticket         | Each ticket links to its corresponding solution                 |
| TC-05   | Ticket description is preserved      | Problem statement is available in Jira                          |
| TC-06   | Acceptance criteria are preserved    | All criteria appear correctly in Jira                           |
| TC-07   | GitHub commit is associated          | The commit is linked to the intended ticket                     |
| TC-08   | Incorrect association is detected    | A solution for another ticket is not incorrectly linked         |
| TC-09   | Missing code is handled              | A ticket without a solution is not falsely marked complete      |
| TC-10   | Duplicate linking is handled         | Repeated synchronization does not create incorrect duplicates   |

**Important:** These are expected behaviors to test, not claims about
features your PM Board already supports. Some behaviors may require your
team to implement explicit integration rules.

## Phase 4: Test incorrect mappings

Don't just test successful connections — test whether the PM Board catches
incorrect ones.

**Scenario A: Correct mapping**

```text
Jira: PMB-101 — Two Sum
GitHub: PMB-101-two-sum.py

Expected: Correct association
```

**Scenario B: Incorrect mapping**

```text
Jira: PMB-101 — Two Sum
GitHub: PMB-104-maximum-subarray.py

Expected: The integration should not incorrectly associate
the Maximum Subarray solution as the Two Sum implementation.
```

**Scenario C: Missing Jira reference**

```text
GitHub: solution.py
Commit message: Add Python solution

Expected: Verify whether the PM Board can identify the
intended Jira ticket or correctly report that the association
cannot be established.
```

**Scenario D: Acceptance criteria mismatch**

```text
Jira: PMB-103 — Binary Search
Acceptance criteria: O(log n) time complexity

GitHub: Implementation uses a linear scan.

Expected: The integration should not treat the presence
of a linked file alone as proof that the acceptance criteria
have been satisfied.
```

Scenario D is particularly useful because **linking code to a ticket and
validating that the code actually satisfies the ticket are two different
capabilities**.

## Phase 5: Final validation checklist

| Validation                                     | Expected |
| ----------------------------------------------- | -------- |
| Five Jira stories created                        | Pass     |
| Five Python solution files committed             | Pass     |
| Every solution has a matching Jira reference      | Pass     |
| Every solution includes complexity analysis       | Pass     |
| All Python test cases pass                        | Pass     |
| Correct Jira–GitHub associations established      | Pass     |
| Incorrect mappings handled appropriately          | Pass     |
| Missing references handled appropriately          | Pass     |
| Acceptance criteria available for verification    | Pass     |
| PM Board displays accurate integration results     | Pass     |

## Why these five problems

1. **Hash map** — Two Sum
2. **Stack** — Valid Parentheses
3. **Binary search** — Binary Search
4. **Dynamic programming (Kadane's)** — Maximum Subarray
5. **Sorting and merging** — Merge Intervals

Five different algorithmic patterns give a more useful test dataset than
five similar problems.

**The key success criterion:** when you open any of the five tickets in
your PM Board, you should be able to identify the correct GitHub solution
and verify that it corresponds to that ticket — not merely that some code
has been linked.
