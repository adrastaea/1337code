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
        if not head or not head.next:
            return

        # half the List
        slow = head
        fast = head
        prev = None # add pointer to track end of first half
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # disconnect first half from second half
        prev.next = None

        # reverse second half
        prev = None # start at none to have an end to reversed list
        curr = slow # start curr at first node
        # once curr is None, the prev node is the new beginning
        while curr:
            # store the next node before changing pointer to next
            next_node = curr.next
            # point curr at prev
            curr.next = prev
            # advance prev and curr
            prev = curr
            curr = next_node
        # notate new reversed list
        r_curr = prev

        # Merge
        prev = head
        curr = head.next
        while curr:
            # store next nodes
            next_node = curr.next
            r_next_node = r_curr.next
            # insert r_curr
            prev.next = r_curr
            r_curr.next = curr
            # advance prev, curr, r_curr
            prev = curr
            curr = next_node
            r_curr = r_next_node
        prev.next = r_curr

    def reorderListConcise(self, head):
        if not head:
            return

        # Step 1: Split the list into two halves
        # slow and fast are start points, fast moves twice as fast as slow
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Now slow is the start point of the second half
        # Reverse the second half
        prev, curr = None, slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 2: Merge the two halves
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

    def reorderListnSquared(self, head: Optional[ListNode]) -> None:
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
