"""
https://leetcode.com/problems/determine-if-two-strings-are-close/

Pattern:
    Hash Map
    Frequency Counting

Determines if two strings are "close" based on allowed operations:
1. Swap any two characters.
2. Transform all occurrences of one existing character into another (and vice versa).

Two strings are close if:
- They contain the exact same set of characters.
- The frequency of characters (regardless of which character) matches.

Args:
    word1 (str): The first string.
    word2 (str): The second string.

Returns:
    bool: True if word1 and word2 are close, False otherwise.

Example:
    closeStrings("abc", "bca")
    True

    closeStrings("a", "aa")
    False

    closeStrings("cabbba", "abbccc")
    True

Constraints:
    - 1 <= len(word1), len(word2) <= 10^5
    - Both strings contain only lowercase English letters.
"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False

        freq1 = {}
        freq2 = {}

        for c in word1:
            freq1[c] = freq1.get(c, 0) + 1
        for c in word2:
            freq2[c] = freq2.get(c, 0) + 1

        return sorted(freq1.values()) == sorted(freq2.values())


solution = Solution()

word1 = "cabbba"
word2 = "abbccc"

result = solution.closeStrings(word1, word2)

print("Word 1:", word1)
print("Word 2:", word2)
print("Are the strings close?", result)
