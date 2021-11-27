# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 07:59:00 2021

"""

class Solution:
    def twoSum(nums: list, target: int) -> list:
    
        num_index_dict = dict()
        for index in range(len(nums)):
            num = nums[index]
            if num in num_index_dict:
                num_index_dict[num].append(index)
            else:
                num_index_dict[num] = [index]
        print(num_index_dict)
        for num in num_index_dict.keys():
            num2 = target - num
            if num == num2:
                if len(num_index_dict[num])>=2:
                    return [num_index_dict[num][0], num_index_dict[num][1]]
            else:                   
                if num2 in num_index_dict:
                    index1 = num_index_dict[num][0]
                    index2 = num_index_dict[target-num][0]
                    return [index1, index2]