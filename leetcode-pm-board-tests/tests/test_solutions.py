"""
Pytest suite covering all five PM Board test cases (PMB-101..PMB-105).

Run with:
    pytest tests/test_solutions.py -v
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "solutions"))


def _load(module_filename: str):
    """Load a solution module whose filename contains hyphens."""
    import importlib.util

    solutions_dir = Path(__file__).resolve().parent.parent / "solutions"
    path = solutions_dir / module_filename
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


two_sum = _load("PMB-101-two-sum.py").two_sum
is_valid = _load("PMB-102-valid-parentheses.py").is_valid
binary_search = _load("PMB-103-binary-search.py").binary_search
max_subarray = _load("PMB-104-maximum-subarray.py").max_subarray
merge_intervals = _load("PMB-105-merge-intervals.py").merge_intervals


class TestPMB101TwoSum:
    def test_basic_pair(self):
        assert two_sum([2, 7, 11, 15], 9) == [0, 1]

    def test_middle_pair(self):
        assert two_sum([3, 2, 4], 6) == [1, 2]

    def test_duplicate_values(self):
        assert two_sum([3, 3], 6) == [0, 1]

    def test_no_solution_raises(self):
        import pytest

        with pytest.raises(ValueError):
            two_sum([1, 2, 3], 100)


class TestPMB102ValidParentheses:
    def test_simple_pairs(self):
        assert is_valid("()") is True
        assert is_valid("()[]{}") is True
        assert is_valid("{[]}") is True

    def test_mismatched_types(self):
        assert is_valid("(]") is False

    def test_wrong_order(self):
        assert is_valid("([)]") is False

    def test_empty_string(self):
        assert is_valid("") is True

    def test_unmatched_closing(self):
        assert is_valid(")") is False


class TestPMB103BinarySearch:
    def test_found_in_middle(self):
        assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4

    def test_not_found(self):
        assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1

    def test_single_element(self):
        assert binary_search([5], 5) == 0

    def test_empty_array(self):
        assert binary_search([], 5) == -1

    def test_first_and_last(self):
        assert binary_search([1, 3, 5, 7], 1) == 0
        assert binary_search([1, 3, 5, 7], 7) == 3


class TestPMB104MaximumSubarray:
    def test_mixed_values(self):
        assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    def test_single_element(self):
        assert max_subarray([1]) == 1

    def test_all_positive(self):
        assert max_subarray([5, 4, -1, 7, 8]) == 23

    def test_all_negative(self):
        assert max_subarray([-3, -2, -5]) == -2

    def test_two_negatives(self):
        assert max_subarray([-1, -2]) == -1


class TestPMB105MergeIntervals:
    def test_overlapping(self):
        assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
            [1, 6],
            [8, 10],
            [15, 18],
        ]

    def test_touching_endpoints(self):
        assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]

    def test_unsorted_input(self):
        assert merge_intervals([[1, 4], [0, 2], [3, 5]]) == [[0, 5]]

    def test_single_interval(self):
        assert merge_intervals([[1, 2]]) == [[1, 2]]

    def test_empty_input(self):
        assert merge_intervals([]) == []
