"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        old_cur = head
        new_head = new_cur = Node(0, None, None)
        old_new_map = dict()
        # Reconstruct the linked list first
        while old_cur:
            new_cur.val = old_cur.val
            old_new_map[old_cur] = new_cur  # Map original node pointer to the new one.

            old_cur = old_cur.next
            if old_cur:
                new_cur.next = Node(0, None, None)
            new_cur = new_cur.next

        # Reconstruct the random pointer
        old_cur = head
        new_cur = new_head
        while old_cur:
            if old_cur.random:
                new_cur.random = old_new_map[old_cur.random]  # grab the new pointer and assign it to the random of this pointer like in the original linked list
            new_cur = new_cur.next
            old_cur = old_cur.next

        return new_head
        