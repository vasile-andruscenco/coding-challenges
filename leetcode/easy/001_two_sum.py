"""
https://leetcode.com/problems/two-sum/description/

    Given an array of integers `nums` and an integer `target`, return the indices of the two numbers
    such that they add up to `target`.

    You may assume that each input has exactly one solution, and you may not use the same element twice.

    The answer can be returned in any order.

    Args:
        nums (List[int]): A list of integers.
        target (int): The target sum.

    Returns:
        List[int]: Indices of the two numbers such that they add up to target.

    Example:
        twoSum([2, 7, 11, 15], 9)
        [0, 1]

        ([3, 2, 4], 6)
        [1, 2]

        ([3, 3], 6)
        [0, 1]

    Constraints:
        - 2 <= len(nums) <= 10^4
        - -10^9 <= nums[i] <= 10^9
        - -10^9 <= target <= 10^9
        - Only one valid answer exists.

    Follow-up:
        Can you come up with an algorithm that has a time complexity less than O(n^2)?
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in result:
                return [result[diff], i]
            result[num] = i

solution = Solution()

nums = [2, 7, 11, 15]
target = 26

output = solution.twoSum(nums, target)

print(output)  # Output: [0, 1]
