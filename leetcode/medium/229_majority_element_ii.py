"""
https://leetcode.com/problems/majority-element-ii/

Pattern:
    Boyer-Moore Voting

Given an integer array `nums` of size n, returns all elements that appear more than
n // 3 times. At most two such elements can exist.

Args:
    nums (List[int]): A non-empty list of integers.

Returns:
    List[int]: The elements appearing more than len(nums) // 3 times, in any order.

Examples:
    majorityElement([3, 2, 3])
    [3]

    majorityElement([1])
    [1]

    majorityElement([1, 2])
    [1, 2]

Constraints:
    - 1 <= len(nums) <= 5 * 10^4
    - -10^9 <= nums[i] <= 10^9

Follow-up:
    Could you solve the problem in linear time and in O(1) space?
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = candidate2 = 0
        count1 = count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        result = []

        if nums.count(candidate1) > len(nums) // 3:
            result.append(candidate1)
        if candidate2 != candidate1 and nums.count(candidate2) > len(nums) // 3:
            result.append(candidate2)

        return result

solution = Solution()

nums = [3, 2, 3]

print("Array:", nums)
print("Majority elements:", solution.majorityElement(nums))  # Output: [3]
