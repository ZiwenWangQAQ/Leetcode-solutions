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

        while head.next and head.next.val == head.val:
            flag = True
            while head.next and head.next.val == head.val:
                head = head.next
                flag = False

            if not flag:
                head = head.next
            if not head:
                return head

        ans = head
        while head.next:
            tmp = head.next
            flag = True
            while tmp.next and tmp.next.val == tmp.val:
                tmp = tmp.next
                flag = False
            if flag:
                head.next = tmp
                head = head.next
            else:
                if tmp.next:
                    head.next = tmp.next
                else:
                    head.next = None
                    break

        return ans