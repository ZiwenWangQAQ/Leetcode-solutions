# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1

        list1_val = list()
        list2_val = list()
        merge_val = list()

        while list1:
            list1_val.append(list1.val)
            list1 = list1.next
        while list2:
            list2_val.append(list2.val)
            list2 = list2.next

        point1 = 0
        point2 = 0
        while point1 < len(list1_val):
            if list1_val[point1] < list2_val[point2]:
                merge_val.append(list1_val[point1])
                point1 += 1
            else:
                merge_val.append(list2_val[point2])
                point2 += 1

            if point1 == len(list1_val):
                for point in range(point2, len(list2_val)):
                    merge_val.append(list2_val[point])
                break
            elif point2 == len(list2_val):
                for point in range(point1, len(list1_val)):
                    merge_val.append(list1_val[point])
                break

        final_list_head = ListNode(merge_val[0])
        final_list = final_list_head

        for point in range(1, len(merge_val)):
            final_list_head.next = ListNode(merge_val[point])
            final_list_head = final_list_head.next

        return final_list
