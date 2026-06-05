# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        
        head = ListNode(-1)
        curr = head

        carry = 0

        while l1 and l2:
            x = l1.val
            y = l2.val

            digit_sum = x + y + carry

            if digit_sum >= 10:
                digit_sum -= 10
                carry = 1
            else:
                carry = 0
            node = ListNode(digit_sum)
            curr.next = node
            curr = curr.next

            l1 = l1.next
            l2 = l2.next
        
        while l1:
            x = l1.val

            digit_sum = x + carry
            if digit_sum >= 10:
                digit_sum -= 10
                carry = 1
            else:
                carry = 0
            node = ListNode(digit_sum)
            curr.next = node
            curr = curr.next

            l1 = l1.next
        
        while l2:
            x = l2.val

            digit_sum = x + carry
            if digit_sum >= 10:
                digit_sum -= 10
                carry = 1
            else:
                carry = 0
            node = ListNode(digit_sum)
            curr.next = node
            curr = curr.next

            l2 = l2.next

        if carry:
            node = ListNode(1)
            curr.next = node
            curr = curr.next

        return head.next