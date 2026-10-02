# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_1, cur_2 = l1, l2
        carry = False
        dummy = cur_new = ListNode()
        while cur_1 and cur_2:
            result = cur_1.val + cur_2.val
            if carry:
                result += 1
            if result > 9:
                carry = True
                cur_new.next = ListNode(val=result-10)
            else:
                carry = False
                cur_new.next = ListNode(val=result)
            cur_new = cur_new.next
            cur_1, cur_2 = cur_1.next, cur_2.next

        if cur_1:
            while cur_1:
                result = cur_1.val
                if carry:
                    result += 1
                if result > 9:
                    carry = True
                    cur_new.next = ListNode(val=result-10)
                else:
                    carry = False
                    cur_new.next = ListNode(val=result)
                cur_new = cur_new.next
                cur_1 = cur_1.next
        elif cur_2:
            while cur_2:
                result = cur_2.val
                if carry:
                    result += 1
                if result > 9:
                    carry = True
                    cur_new.next = ListNode(val=result-10)
                else:
                    carry = False
                    cur_new.next = ListNode(val=result)
                cur_new = cur_new.next
                cur_2 = cur_2.next
        if carry:
            cur_new.next = ListNode(val=1)
        return dummy.next
       