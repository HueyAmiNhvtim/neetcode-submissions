# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur_pos = count = 0
        cur = head
        # Count the number of elements in the linked list
        while cur:
            count += 1
            cur = cur.next

        dummy = ListNode(next=head)
        cur = head
        prev = dummy
        while cur:
            next = cur.next
            cur_pos += 1
            if (count - n + 1) == cur_pos:
                # Remove the node
                prev.next = next
                break
            prev = cur
            cur = cur.next

        return dummy.next
        