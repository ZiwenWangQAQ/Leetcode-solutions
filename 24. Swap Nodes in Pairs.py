# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        final_head = head.next

        pre = head
        middle = head.next
        last = head.next.next
        middle.next = head
        head.next = last

        if not final_head.next.next:
            return final_head

        while head.next.next:
            pre = head
            middle = head.next
            last = head.next.next
            pre.next = last
            middle.next = last.next
            last.next = middle
            head = head.next.next
            if not head:
                break
            if not head.next:
                break

        return final_head
