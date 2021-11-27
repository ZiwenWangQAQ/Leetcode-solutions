# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 07:59:00 2021

"""

class Solution:
    def twoSum(nums: list, target: int) -> list:
    
        num_index_dict = dict()
        for index in range(len(nums)):
            num = nums[index]
            num2 = target - num
            if num2 in num_index_dict:
                return [num_index_dict[num2], index]
            num_index_dict[num] = index
