"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/

Given two strings `str1` and `str2`, returns the largest string `x` such that
both `str1` and `str2` are a concatenation of `x` one or more times.

Args:
    str1 (str): The first string.
    str2 (str): The second string.

Returns:
    str: The greatest common divisor string, or an empty string if none exists.

Logic:
    - If str1 + str2 != str2 + str1, no common divisor exists.
    - Otherwise, the GCD of the lengths of the strings gives the length of the common divisor.

Example:
    gcdOfStrings("ABCABC", "ABC")
    "ABC"

    gcdOfStrings("ABABAB", "ABAB")
    "AB"

    gcdOfStrings("LEET", "CODE")
    ""

Constraints:
    - 1 <= len(str1), len(str2) <= 1000
    - str1 and str2 consist of uppercase English letters only.
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        def compute_gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        gcd_length = compute_gcd(len(str1), len(str2))
        return str1[:gcd_length]

solution = Solution()

str1 = "ABABAB"
str2 = "ABAB"

result = solution.gcdOfStrings(str1, str2)

print("String 1:", str1)
print("String 2:", str2)
print("Greatest common divisor of strings:", result)
