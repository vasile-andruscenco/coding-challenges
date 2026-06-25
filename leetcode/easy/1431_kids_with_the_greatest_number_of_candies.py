"""
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

Determines which kids can have the greatest number of candies if they receive all the extra candies.

For each child in the list `candies`, checks if giving them `extraCandies` would result in a total
greater than or equal to the maximum number of candies any child currently has.

Args:
    candies (List[int]): A list where candies[i] represents the number of candies the i-th kid has.
    extraCandies (int): The number of extra candies available to give.

Returns:
    List[bool]: A list of booleans where result[i] is True if kid i can have the greatest number of candies.

Example:
    kidsWithCandies([2,3,5,1,3], 3)
    [True, True, True, False, True]

Constraints:
    - 2 <= len(candies) <= 100
    - 1 <= candies[i] <= 100
    - 1 <= extraCandies <= 50
"""

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]

solution = Solution()

candies = [2, 3, 5, 1, 3]
extraCandies = 3

result = solution.kidsWithCandies(candies, extraCandies)

print("Candies per kid:", candies)
print("Extra candies:", extraCandies)
print("Can have greatest number of candies:", result)
