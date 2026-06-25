"""
https://leetcode.com/problems/sqrtx/

Pattern:
    Binary Search
    Search on Answer

Computes the integer (floor) square root of a non-negative integer `x`,
i.e. the largest integer `k` such that `k * k <= x`. The fractional part
of the true square root is truncated.

The solution applies binary search on the answer: the candidate result lives
in the range [0, x], and the predicate "mid * mid <= x" is monotonic, so we
can discard half of the search space at every step.

Args:
    x (int): A non-negative integer.

Returns:
    int: The floor of the square root of `x`.

Example:
    Input: x = 4
    Output: 2

    Input: x = 8
    Output: 2  # sqrt(8) = 2.828..., truncated to 2

Constraints:
    - 0 <= x <= 2^31 - 1
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        result = 0

        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid <= x:
                result = mid       # mid is a valid answer; try to grow it
                left = mid + 1
            else:
                right = mid - 1

        return result


solution = Solution()

print(solution.mySqrt(4))  # Output: 2
print(solution.mySqrt(8))  # Output: 2
