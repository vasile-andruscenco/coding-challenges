"""
https://leetcode.com/problems/merge-strings-alternately/

Merges two strings by alternating characters from each. Starts with the first character
from `word1`, then the first from `word2`, and so on. If one string is longer,
appends the remainder at the end.

Args:
    word1 (str): The first input string.
    word2 (str): The second input string.

Returns:
    str: A new string formed by alternating characters from both inputs.

Example:
    mergeAlternately("abc", "pqr")
    'apbqcr'

    mergeAlternately("ab", "pqrs")
    'apbqrs'

    mergeAlternately("abcd", "pq")
    'apbqcd'

Constraints:
    - 1 <= len(word1), len(word2) <= 100
    - word1 and word2 contain only lowercase English letters.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        merged = ''.join(word1[i] + word2[i] for i in range(min_len))
        return merged + word1[min_len:] + word2[min_len:]

solution = Solution()

word1 = "abc"
word2 = "pqr"

merged = solution.mergeAlternately(word1, word2)

print("Word 1:", word1)
print("Word 2:", word2)
print("Merged string:", merged)
