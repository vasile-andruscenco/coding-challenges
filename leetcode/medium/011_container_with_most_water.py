"""
https://leetcode.com/problems/container-with-most-water/

Finds two vertical lines that together with the x-axis form a container
capable of storing the maximum amount of water.

The amount of water is calculated by multiplying the distance between two lines
by the height of the shorter line. The solution uses the Two Pointers pattern.

Args:
    height (List[int]): A list where height[i] represents the height of the i-th vertical line.

Returns:
    int: The maximum amount of water the container can store.

Example:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49

    Input: height = [1,1]
    Output: 1

Constraints:
    - 2 <= len(height) <= 10^5
    - 0 <= height[i] <= 10^4
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height

            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


solution = Solution()
height = [1,8,6,2,5,4,8,3,7]

print(solution.maxArea(height))  # Output: 49
