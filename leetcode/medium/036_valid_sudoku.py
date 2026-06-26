"""
https://leetcode.com/problems/valid-sudoku/

Pattern:
    Hash Map
    Duplicate Detection
    Matrix Traversal

Determines whether a partially filled 9 x 9 Sudoku board is valid. Only the filled
cells are validated against the three Sudoku rules; the board does not need to be
solvable.

A board is valid when:
- each row contains the digits 1-9 without repetition,
- each column contains the digits 1-9 without repetition,
- each of the nine 3 x 3 sub-boxes contains the digits 1-9 without repetition.

Empty cells are represented by '.' and are ignored.

Args:
    board (List[List[str]]): A 9 x 9 grid where each cell holds a digit '1'-'9'
        or '.' for an empty cell.

Returns:
    bool: True if the board is valid according to the rules above, False otherwise.

Example:
    Input:
        board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"],
        ]
    Output:
        True

    Input: same board as above, but with the top-left "5" changed to "8"
    Output:
        False  # two 8s now share the first column and the top-left 3 x 3 box

Constraints:
    - board.length == 9
    - board[i].length == 9
    - board[i][j] is a digit '1'-'9' or '.'
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for row_index, row in enumerate(board):
            for col_index, value in enumerate(row):
                if value == ".":
                    continue

                row_key = (value, "row", row_index)
                col_key = (value, "col", col_index)
                box_key = (value, "box", row_index // 3, col_index // 3)

                if row_key in seen or col_key in seen or box_key in seen:
                    return False

                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

        return True

        # for row in board:
        #     seen = set()
        #     for value in row:
        #         if value == ".":
        #             continue
        #         if value in seen:
        #             return False
        #
        #         seen.add(value)
        #
        # for col in range(len(board[0])):
        #     seen = set()
        #
        #     for row in board:
        #         value = row[col]
        #         if value == ".":
        #             continue
        #         if value in seen:
        #             return False
        #
        #         seen.add(value)
        #
        # for box_row in range(0, 9, 3):
        #     for box_col in range(0, 9, 3):
        #         seen = set()
        #
        #         for row in range(box_row, box_row + 3):
        #             for col in range(box_col, box_col + 3):
        #                 value = board[row][col]
        #                 if value == ".":
        #                     continue
        #                 if value in seen:
        #                     return False
        #
        #                 seen.add(value)
        #
        # return True


solution = Solution()

board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"],
        ]

print("Is valid Sudoku:", solution.isValidSudoku(board))  # Output: True
