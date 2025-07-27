"""
https://leetcode.com/problems/zigzag-conversion/

Converts a given string into a zigzag pattern across a specified number of rows,
then reads the characters row by row to produce the final converted string.

The zigzag pattern means writing characters in a diagonal-down and then diagonal-up manner
across multiple rows. For example, for 3 rows, the string is written like this:

Row 0: chars at indices 0, 4, 8, ...
Row 1: chars at indices 1, 3, 5, 7, ...
Row 2: chars at indices 2, 6, 10, ...

Args:
    s (str): The input string consisting of English letters, ',' and '.'.
    numRows (int): The number of rows in the zigzag pattern (1 <= numRows <= 1000).

Returns:
    str: The converted string formed by reading the zigzag pattern row by row.

Examples:
    Solution().convert("PAYPALISHIRING", 3)
    # Output: "PAHNAPLSIIGYIR"

    Solution().convert("PAYPALISHIRING", 4)
    # Output: "PINALSIGYAHRPI"

    Solution().convert("A", 1)
    # Output: "A"

Constraints:
    - 1 <= len(s) <= 1000
    - 1 <= numRows <= 1000
    - s consists of English letters (upper and lower case), ',' and '.'
"""

class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        return ''.join(rows)
