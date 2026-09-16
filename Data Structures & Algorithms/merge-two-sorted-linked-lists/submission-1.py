# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        n1, n2 = list1, list2
        if n1.val < n2.val:
            head_result = n1
            n1 = n1.next
        else:
            head_result = n2
            n2 = n2.next
        cur_result = head_result
        while n1 is not None and n2 is not None:
            if n1.val < n2.val:
                cur_result.next = n1
                n1 = n1.next
            else:
                cur_result.next = n2
                n2 = n2.next
            cur_result = cur_result.next

        while n1 is not None:
            cur_result.next = n1
            n1 = n1.next
            cur_result = cur_result.next

        while n2 is not None:
            cur_result.next = n2
            n2 = n2.next
            cur_result = cur_result.next


        return head_result