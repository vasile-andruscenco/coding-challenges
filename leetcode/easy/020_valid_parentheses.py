"""
https://leetcode.com/problems/valid-parentheses/

Pattern:
    Stack

Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']',
determines whether the input string is valid.

A string is valid when:
- every open bracket is closed by a bracket of the same type,
- open brackets are closed in the correct order,
- every close bracket has a matching open bracket of the same type.

Args:
    s (str): A string consisting only of the characters '()[]{}'.

Returns:
    bool: True if the brackets are balanced and correctly nested, False otherwise.

Examples:
    isValid("()")
    True

    isValid("()[]{}")
    True

    isValid("(]")
    False

    isValid("([])")
    True

    isValid("([)]")
    False

Constraints:
    - 1 <= len(s) <= 10^4
    - s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char in pairs:
                if not stack:
                    return False
                if pairs[char] != stack.pop():
                    return False
            else:
                stack.append(char)

        return not stack


solution = Solution()

s = "([])"
# s = ("(]")

print("Input:", s)
print("Valid:", solution.isValid(s))  # Output: True
