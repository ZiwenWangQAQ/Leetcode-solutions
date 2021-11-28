# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        num2 = 0
        multiple = 1
        
        while l1:
            num1 = num1+l1.val*multiple
            multiple *= 10
            l1 = l1.next
        
        multiple = 1
        while l2:
            num2 = num2+l2.val*multiple
            multiple *= 10
            l2 = l2.next
        
        ans_num = num1 + num2
        
        if ans_num == 0:
            return ListNode(0)
        
        num_list = list()
        while ans_num:
            num_list.append(ans_num%10)
            ans_num = ans_num//10

        res = ListNode()
        ans = res
        for index in range(len(num_list)):
            num = num_list[index]
            res.val = num
            if index!= len(num_list)-1:
                res.next = ListNode()
            res = res.next
        
        return ans
            
        
        
        
            