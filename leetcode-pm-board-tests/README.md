# leetcode-pm-board-tests

Five LeetCode-style test cases used to validate a **PM Board** integration
that bridges Jira tickets to their corresponding GitHub code solutions.

Each test case has three parts:

- **Jira** (`jira_tickets/`): summary, description, problem statement,
  functional requirements, and acceptance criteria — ready to paste into
  real Jira tickets.
- **GitHub** (`solutions/`): a Python solution with algorithm notes, time
  and space complexity, and inline test cases.
- **Tests** (`tests/test_solutions.py`): a pytest suite covering all five
  solutions.

See [`TESTING.md`](TESTING.md) for the full end-to-end PM Board testing
procedure (branch naming, Jira↔GitHub verification checklist, incorrect
mapping scenarios, and the final validation checklist).

## Structure

```text
leetcode-pm-board-tests/
├── README.md
├── TESTING.md
├── jira_tickets/
│   ├── PMB-101-two-sum.md
│   ├── PMB-102-valid-parentheses.md
│   ├── PMB-103-binary-search.md
│   ├── PMB-104-maximum-subarray.md
│   └── PMB-105-merge-intervals.md
├── solutions/
│   ├── PMB-101-two-sum.py
│   ├── PMB-102-valid-parentheses.py
│   ├── PMB-103-binary-search.py
│   ├── PMB-104-maximum-subarray.py
│   └── PMB-105-merge-intervals.py
└── tests/
    └── test_solutions.py
```

## Problems covered

| Jira ID | Summary           | Algorithm          |
| ------- | ------------------ | -------------------- |
| PMB-101 | Two Sum             | Hash map             |
| PMB-102 | Valid Parentheses   | Stack                |
| PMB-103 | Binary Search        | Binary search         |
| PMB-104 | Maximum Subarray     | Kadane's algorithm    |
| PMB-105 | Merge Intervals      | Sorting               |

## Running the tests

```bash
# Run an individual solution's self-checks
python solutions/PMB-101-two-sum.py

# Run the full pytest suite
pytest tests/test_solutions.py -v
```
