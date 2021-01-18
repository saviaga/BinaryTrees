from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_string = deque()
        res = 0
        l,r = 0,0
        
        while l < len(s):
            if s[l] not in longest_string:
                longest_string.append(s[l])
                l+=1
                
            else:
                
                longest_string.popleft()
                
                r += 1
            res = max(res, l - r)
        return res            
           
        
        
            
        
