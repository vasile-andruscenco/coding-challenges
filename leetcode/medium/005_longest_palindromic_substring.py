"""
https://leetcode.com/problems/longest-palindromic-substring/

Finds the longest palindromic substring in the given string.

A palindrome is a string that reads the same forward and backward.
This function expands around each character (as center) to find both odd- and even-length palindromes,
and returns the longest one found.

Args:
    s (str): A non-empty string consisting of digits and/or English letters. 1 <= len(s) <= 1000

Returns:
    str: The longest substring of `s` that is a palindrome.

Examples:
    Solution().longestPalindrome("babad")
    'bab'  # or 'aba', both are valid

    Solution().longestPalindrome("cbbd")
    'bb'

    Solution().longestPalindrome("a")
    'a'

    Solution().longestPalindrome("ac")
    'a'  # or 'c'
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_from_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            odd = expand_from_center(i, i)
            if len(odd) > len(longest):
                longest = odd

            even = expand_from_center(i, i + 1)
            if len(even) > len(longest):
                longest = even

        return longest

print("Example 1:", Solution().longestPalindrome("babad"))  # Expected: 'bab' or 'aba'
print("Example 2:", Solution().longestPalindrome("cbbd"))   # Expected: 'bb'
print("Example 3:", Solution().longestPalindrome("a"))      # Expected: 'a'
print("Example 4:", Solution().longestPalindrome("ac"))     # Expected: 'a' or 'c'
print("Example 5:", Solution().longestPalindrome("forgeeksskeegfor"))  # Expected: 'geeksskeeg'
