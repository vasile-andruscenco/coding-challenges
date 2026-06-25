"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Removes all occurrences of `val` from the list `nums` in-place and returns the number of remaining elements.

The first `k` elements of the array `nums` will be modified to contain the elements not equal to `val`,
and their order may change. The values beyond index `k` are irrelevant.

Args:
    nums (List[int]): The list of integers from which to remove `val`.
    val (int): The integer value to remove from `nums`.

Returns:
    int: The number of elements not equal to `val` (denoted as `k`).

Example:
    nums = [3, 2, 2, 3]
    val = 3
    k = removeElement(nums, val)
    k
    2
    nums[:k]
    [2, 2]

    nums = [0,1,2,2,3,0,4,2]
    val = 2
    k = removeElement(nums, val)
    k
    5
    sorted(nums[:k])  # Can be in any order
    [0, 0, 1, 3, 4]

Constraints:
    - 0 <= len(nums) <= 100
    - 0 <= nums[i] <= 50
    - 0 <= val <= 100

Notes:
    - The operation must be performed in-place with O(1) extra memory.
    - The order of elements can be changed.
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

solution = Solution()

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

k = solution.removeElement(nums, val)

print("Number of elements kept:", k)
print("Elements without the value 2:", nums[:k])
