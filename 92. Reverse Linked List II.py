# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        ans = head
        left_constant = left

        # deal with the speical case that there is no left part
        if left == 1:
            left_part = None
            middle_part = head
        # get the left part and middle part
        else:
            while left > 2:
                left = left - 1
                head = head.next
            left_part = head
            middle_part = head.next
            head.next = None

        # deal with the special case that there is no middle_part
        if not middle_part:
            return ans

        # take the right part
        head = middle_part
        right = right - left_constant
        while right:
            head = head.next
            right = right - 1
        right_part = head.next
        head.next = None

        # if the length of middle_part is larger than 2, then make the middle part reversed
        if middle_part.next:
            tmp = middle_part.next
            middle_part.next = None
            while tmp.next:
                last = tmp.next
                tmp.next = middle_part
                middle_part = tmp
                tmp = last
            tmp.next = middle_part
            middle_part = tmp

        # join the left part with the middle part
        if left_part:
            left_part.next = middle_part
        else:
            ans = middle_part

        # join the middle_part with the right part
        while middle_part.next:
            middle_part = middle_part.next
        middle_part.next = right_part

        return ans
