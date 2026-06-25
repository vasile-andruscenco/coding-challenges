"""
https://leetcode.com/problems/merge-sorted-array/

Merges two sorted integer arrays into a single sorted array in-place.

The first `m` elements of `nums1` contain valid values, while the remaining
`n` elements are placeholders (0) that provide enough space for all elements
from `nums2`. The merged result is stored directly in `nums1`.

Args:
    nums1 (List[int]): The destination array with length `m + n`, where the
        first `m` elements are sorted values and the remaining elements are placeholders.
    m (int): The number of valid elements in `nums1`.
    nums2 (List[int]): A sorted array containing `n` elements.
    n (int): The number of elements in `nums2`.

Returns:
    None: The function modifies `nums1` in-place and does not return a value.

Example:
    Input:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6], n = 3

    Output:
        nums1 = [1,2,2,3,5,6]

    Input:
        nums1 = [1], m = 1
        nums2 = [], n = 0

    Output:
        nums1 = [1]

    Input:
        nums1 = [0], m = 0
        nums2 = [1], n = 1

    Output:
        nums1 = [1]

Constraints:
    - nums1.length == m + n
    - nums2.length == n
    - 0 <= m, n <= 200
    - 1 <= m + n <= 200
    - -10^9 <= nums1[i], nums2[j] <= 10^9
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
