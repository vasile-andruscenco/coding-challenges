"""
https://leetcode.com/problems/add-two-numbers/description/

Adds two non-negative integers represented as reversed linked lists and returns the sum
as a new reversed linked list.

Each node in the input lists contains a single digit, and the digits are stored in reverse order.
The result should also be a linked list in reverse order, with no leading zeros.

This function handles carries across digits (e.g., 9 + 1 → 0 carry 1) and supports different lengths.

Args:
    first_number (ListNode): The head of the first linked list representing an integer.
    second_number (ListNode): The head of the second linked list representing an integer.

Returns:
    ListNode: The head of the resulting linked list representing the sum.

Example:
    Input: first_number = [2, 4, 3], second_number = [5, 6, 4]
    Output: [7, 0, 8]  # Because 342 + 465 = 807

    Input: first_number = [0], second_number = [0]
    Output: [0]

    Input: first_number = [9,9,9,9,9,9,9], second_number = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]  # Because 9999999 + 9999 = 10009998

Constraints:
    - The number of nodes in each linked list is in the range [1, 100].
    - Each node contains a digit in the range [0, 9].
    - There are no leading zeros in the input numbers, except the number 0 itself.
"""

from typing import Optional, List

class ListNode:
    def __init__(self, value: int = 0, next_node: Optional['ListNode'] = None):
        self.val = value
        self.next = next_node

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def addTwoNumbers(
        self,
        first_number: Optional[ListNode],
        second_number: Optional[ListNode]
    ) -> Optional[ListNode]:
        result_head = ListNode(0)
        result_tail = result_head
        carry = 0

        while first_number or second_number or carry:
            digit1 = first_number.val if first_number else 0
            digit2 = second_number.val if second_number else 0

            total = digit1 + digit2 + carry
            carry = total // 10
            current_digit = total % 10

            result_tail.next = ListNode(current_digit)
            result_tail = result_tail.next

            if first_number:
                first_number = first_number.next
            if second_number:
                second_number = second_number.next

        return result_head.next


def list_to_linked_list(numbers: List[int]) -> Optional[ListNode]:
    head = ListNode()
    tail = head
    for number in numbers:
        tail.next = ListNode(number)
        tail = tail.next
    return head.next


def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values


first_number = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
second_number = list_to_linked_list([9, 9, 9, 9])

solution = Solution()
sum_linked_list = solution.addTwoNumbers(first_number, second_number)
result_as_list = linked_list_to_list(sum_linked_list)

print("Result as list:", result_as_list)
