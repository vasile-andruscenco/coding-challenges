"""
https://leetcode.com/problems/can-place-flowers/

Determines if `n` new flowers can be planted in the flowerbed without violating
the no-adjacent-flowers rule.

Args:
    flowerbed (List[int]): A list representing the flowerbed, where 0 means empty and 1 means occupied.
    n (int): The number of flowers to plant.

Returns:
    bool: True if `n` flowers can be planted without breaking the rule, False otherwise.

Rules:
    - A flower can be planted in a plot only if both adjacent plots are empty or out of bounds.

Example:
    canPlaceFlowers([1,0,0,0,1], 1)
    True

    canPlaceFlowers([1,0,0,0,1], 2)
    False

Constraints:
    - 1 <= len(flowerbed) <= 2 * 10^4
    - flowerbed[i] is 0 or 1
    - 0 <= n <= len(flowerbed)
"""

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)

                if empty_left and empty_right:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True

        return count >= n

solution = Solution()

flowerbed = [1, 0, 0, 0, 1]
n = 1

result = solution.canPlaceFlowers(flowerbed, n)

print("Flowerbed:", flowerbed)
print("Can place", n, "flowers?", result)
