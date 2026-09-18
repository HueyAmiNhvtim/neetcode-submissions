# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # We should know when the cutoff point is
        tortoise = hare = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
        # Now tortoise.next is the beginning node of the later half of the linked list
        # Reverse linked-list the later half
        prev = None
        cur = tortoise.next
        tortoise.next = None
        while cur is not None:
            next = cur.next
            cur.next = prev

            prev = cur
            cur = next
            
        # Now reorder it properly in accordance with the demand
        cur1 = head
        cur2 = prev
        while cur1 and cur2:
            next1 = cur1.next
            next2 = cur2.next
            cur1.next = cur2

            cur1.next.next = next1
            cur1 = next1
            cur2 = next2
        