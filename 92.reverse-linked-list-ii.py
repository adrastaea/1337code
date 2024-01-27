#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next or left == right:
            return head

        prev = None
        curr = head
        count = 1
        while count <= right:
            if count == left:
                l_connector = prev
                reversed_end = curr
            if count == right:
                r_connector = curr.next
                reversed_begin = curr
            if count - 1 >= left and count <= right:
                next_node = curr.next
                curr.next = prev
                prev, curr = curr, next_node
            else:
                prev, curr = curr, curr.next
            count += 1

        if l_connector:
            l_connector.next = reversed_begin

        reversed_end.next = r_connector
        if left == 1:
            return reversed_begin
        return head


# @lc code=end
