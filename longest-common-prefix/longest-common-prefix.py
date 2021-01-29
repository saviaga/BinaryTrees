class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        
        longest = max(strs)
        
        for i in range(len(strs)-1):
            p1,p2=0,0
            prefix = ''
            while p1< len( strs[i]) and p2 < len( strs[i+1]):
                if strs[i][p1] == strs[i+1][p2]:
                    prefix+=strs[i][p1]
                    p1+=1
                    p2+=1
                else:
                    break
                
            if len(prefix) <= len(longest):
                longest = prefix
                    
        
        return longest                    
            