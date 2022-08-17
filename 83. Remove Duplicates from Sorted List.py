# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head
        if not head.next:
            return head

        val_set = set()
        ans = head
        while head.next:
            val_set.add(head.val)
            if head.next.val in val_set:
                head.next = head.next.next
            else:
                head = head.next
        return ans
