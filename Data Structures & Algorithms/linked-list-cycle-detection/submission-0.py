# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = hare = head
        while tortoise is not None and hare is not None:
            tortoise = tortoise.next
            if hare.next is None:
                break
            hare = hare.next.next
            if tortoise == hare:
                return True
        return False