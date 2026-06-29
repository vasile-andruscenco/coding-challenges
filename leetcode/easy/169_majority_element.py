"""
https://leetcode.com/problems/majority-element/

Pattern:
    Boyer-Moore Voting

Given an array `nums` of size n, returns the majority element — the element that
appears more than n // 2 times. The majority element is guaranteed to always exist
in the array.

Args:
    nums (List[int]): A non-empty list of integers whose majority element is sought.

Returns:
    int: The element that appears more than len(nums) // 2 times.

Examples:
    majorityElement([3, 2, 3])
    3

    majorityElement([2, 2, 1, 1, 1, 2, 2])
    2

Constraints:
    - n == len(nums)
    - 1 <= n <= 5 * 10^4
    - -10^9 <= nums[i] <= 10^9

Follow-up:
    Could you solve the problem in linear time and in O(1) space?
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

solution = Solution()

nums = [2, 2, 1, 1, 1, 2, 2]

print("Array:", nums)
print("Majority element:", solution.majorityElement(nums))  # Output: 2
