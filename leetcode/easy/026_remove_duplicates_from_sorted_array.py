"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Pattern:
    Two Pointers
    Fast & Slow Pointers

Removes duplicates from a sorted array `nums` in-place such that each unique element appears only once.
The relative order of the elements is preserved. Returns the number of unique elements.

The function modifies the input array `nums` such that the first `k` elements are the unique values,
and the remaining elements beyond `k` are not important.

Args:
    nums (List[int]): A list of integers sorted in non-decreasing order.

Returns:
    int: The number of unique elements `k`.

Example:
    nums = [1, 1, 2]
    k = removeDuplicates(nums)
    k
    2
    nums[:k]
    [1, 2]

    nums = [0,0,1,1,1,2,2,3,3,4]
    k = removeDuplicates(nums)
    k
    5
    nums[:k]
    [0, 1, 2, 3, 4]

Constraints:
    - 1 <= len(nums) <= 3 * 10^4
    - -100 <= nums[i] <= 100
    - nums is sorted in non-decreasing order.

Notes:
    - The solution must perform in-place with O(1) extra memory.
    - The elements beyond the first `k` positions in `nums` may be any value and are not checked.
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

solution = Solution()

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

k = solution.removeDuplicates(nums)

print("Number of unique elements:", k)
print("Unique elements:", nums[:k])
