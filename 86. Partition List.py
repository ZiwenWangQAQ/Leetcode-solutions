# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head, x):
        if not head:
            return head
        if not head.next:
            return head

        head_small = None
        head_big = None
        small_start = None
        big_start = None

        while head:
            if head.val < x:
                if not head_small:
                    head_small = head
                    small_start = head
                else:
                    head_small.next = head
                    head_small = head_small.next
                if head_big:
                    head_big.next = None
            else:
                if not head_big:
                    head_big = head
                    big_start = head
                else:
                    head_big.next = head
                    head_big = head_big.next
                if head_small:
                    head_small.next = None
            head = head.next

        if not small_start:
            return big_start
        if not big_start:
            return small_start

        ans = small_start
        while small_start.next:
            small_start = small_start.next
        small_start.next = big_start

        return ans
