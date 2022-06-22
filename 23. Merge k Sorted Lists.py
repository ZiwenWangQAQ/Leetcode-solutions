# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        all_values = []
        for list in lists:
            while list:
                all_values.append(list.val)
                list = list.next

        all_values.sort()
        if not all_values:
            return None

        final_list_head = ListNode(all_values[0])
        final_list = final_list_head

        for point in range(1, len(all_values)):
            final_list_head.next = ListNode(all_values[point])
            final_list_head = final_list_head.next

        return final_list
