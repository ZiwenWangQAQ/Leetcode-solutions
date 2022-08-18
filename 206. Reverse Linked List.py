# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if not head:
            return head
        if not head.next:
            return head

        tmp = head.next
        head.next = None
        while tmp.next:
            last = tmp.next
            tmp.next = head
            head = tmp
            tmp = last
        tmp.next = head

        return tmp
