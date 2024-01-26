#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Modify to L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
        if head.next is None:
            return

        l = head
        r = l.next

        # while p1 has a next
        while r.next:
            # walk r  to end of list
            while r.next:
                # set p2 to node before r
                p2 = r
                r = r.next
            # drop last link
            p2.next = None
            # advance p1
            p1 = l.next

            # point Li at Ln-i and Ln-1 and Li+1
            r.next = p1
            l.next = r

            # move l up
            l = p1
            r = p1
            if p1.next == p2:
                break

# @lc code=end
