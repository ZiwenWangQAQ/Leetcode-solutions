# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k):
        if not k:
            return head

        if not head:
            return head

        if not head.next:
            return head

        tmp = head
        length = 1
        while tmp.next:
            length += 1
            tmp = tmp.next

        k = length - k % length

        if k == length:
            return head

        tmp = head
        while k - 1:
            head = head.next
            k -= 1
        point = head.next
        head.next = None

        ans = point
        while point.next:
            point = point.next
        point.next = tmp

        return ans
