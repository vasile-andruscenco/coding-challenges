"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Pattern:
    Sliding Window
    Variable-size Window

Finds the length of the longest substring without repeating characters.

A substring is a contiguous sequence of characters within a string.
This function uses a sliding window approach to keep track of characters
in the current window and updates the maximum length found.

Args:
    s (str): The input string consisting of English letters, digits, symbols, or spaces.

Returns:
    int: The length of the longest substring with all unique characters.

Examples:
    Solution().lengthOfLongestSubstring("abcabcbb")
    3  # "abc"

    Solution().lengthOfLongestSubstring("bbbbb")
    1  # "b"

    Solution().lengthOfLongestSubstring("pwwkew")
    3  # "wke"
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

solution = Solution()

print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(solution.lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(solution.lengthOfLongestSubstring("pwwkew"))    # Output: 3
print(solution.lengthOfLongestSubstring(""))          # Output: 0
print(solution.lengthOfLongestSubstring("abcdefg"))   # Output: 7
print(solution.lengthOfLongestSubstring("abba"))      # Output: 2
