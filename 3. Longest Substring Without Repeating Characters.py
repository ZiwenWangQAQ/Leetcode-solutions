class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_index_dict = dict()
        tmp_start_index = 0
        max_len = 0
        tmp_len = 0
        
        for index in range(len(s)):  
            
            char = s[index]       
           
            if (char in char_index_dict) and (char_index_dict[char] >= tmp_start_index):
                max_len = max(max_len,tmp_len)
                tmp_start_index = char_index_dict[char]
                tmp_len = index - tmp_start_index                
                
            else:
                tmp_len += 1

            char_index_dict[char] = index

        max_len = max(max_len, tmp_len)
        return max_len            
            
        
        
        
            