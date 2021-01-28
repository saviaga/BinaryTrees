class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
    #    s = "axc", 
    #    t = "ahbgdc"
        
       # T, F,
        ps,pt =0,0
       # subsequence = True
        while ps<len(s) and pt<len(t):
            if s[ps] == t[pt]:
                ps+=1
                pt+=1
                
            else: 
                pt+=1
           
             
        if pt==len(t) and ps<len(s):
            return False
        return True
            
            
            
        
                
        