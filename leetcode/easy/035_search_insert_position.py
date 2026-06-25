"""
https://leetcode.com/problems/search-insert-position/

Pattern:
    Binary Search

Given a sorted list of distinct integers `nums` and a target integer `target`, returns the index
if the target is found. If not, returns the index where it would be inserted to maintain the order.

The algorithm runs in O(log n) time using binary search.

Args:
    nums (List[int]): A list of sorted, distinct integers.
    target (int): The target value to search or insert.

Returns:
    int: The index of the found target or the index where it should be inserted.

Examples:
    searchInsert([1, 3, 5, 6], 5)
    2

    searchInsert([1, 3, 5, 6], 2)
    1

    searchInsert([1, 3, 5, 6], 7)
    4

Constraints:
    - 1 <= len(nums) <= 10^4
    - -10^4 <= nums[i] <= 10^4
    - nums contains distinct values sorted in ascending order
    - -10^4 <= target <= 10^4
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

solution = Solution()

nums = [1, 3, 5, 6]
target = 2

position = solution.searchInsert(nums, target)

print("Target:", target)
print("Array:", nums)
print("Insert/Search Position:", position)
