"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Removes duplicates from a sorted array in-place so that each unique element
appears at most twice. The relative order of the elements is preserved.

The function modifies the input array `nums` so that the first `k` elements
contain the final valid result. Elements beyond the first `k` positions are
irrelevant and may contain any values.

Args:
    nums (List[int]): A list of integers sorted in non-decreasing order.

Returns:
    int: The number of valid elements `k` after removing extra duplicates.

Example:
    Input: nums = [1, 1, 1, 2, 2, 3]
    Output: 5, nums = [1, 1, 2, 2, 3, _]

    Input: nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    Output: 7, nums = [0, 0, 1, 1, 2, 3, 3, _, _]

Constraints:
    - 1 <= len(nums) <= 3 * 10^4
    - -10^4 <= nums[i] <= 10^4
    - nums is sorted in non-decreasing order.

Notes:
    - The solution must modify `nums` in-place.
    - The solution must use O(1) extra memory.
    - Each unique element may appear at most twice.
    - Only the first `k` elements are checked by the judge.
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0

        for number in nums:
            if index < 2 or number != nums[index - 2]:
                nums[index] = number
                index += 1

        return index
