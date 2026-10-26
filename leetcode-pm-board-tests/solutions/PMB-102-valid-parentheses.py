"""
Jira: PMB-102
Title: Valid Parentheses Using a Stack

Algorithm:
1. Push every opening bracket onto a stack.
2. For each closing bracket, check the stack's top element.
3. Reject mismatched brackets or closing brackets without an opener.
4. Return True if the stack is empty at the end.

Time Complexity: O(n)
Space Complexity: O(n)
"""


def is_valid(s: str) -> bool:
    stack = []
    matching = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for char in s:
        if char in matching:
            if not stack or stack.pop() != matching[char]:
                return False
        else:
            stack.append(char)

    return len(stack) == 0


if __name__ == "__main__":
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    assert is_valid("{[]}") is True
    assert is_valid("") is True
    assert is_valid(")") is False

    print("PMB-102: All tests passed!")
