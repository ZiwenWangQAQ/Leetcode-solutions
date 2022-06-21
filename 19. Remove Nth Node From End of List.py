# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        if not head:
            return head

        head2 = head
        length = 1
        while head.next:
            length += 1
            head = head.next

        if n > length:
            return head2

        if n == length:
            return head2.next

        ans = head2
        place_pre = length - n - 1
        while place_pre:
            head2 = head2.next
            place_pre -= 1
        head2.next = head2.next.next

        return ans