class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if len(s)<=1:
            return True
        
        
        filter_s = filter(lambda ch: ch.isalnum(), s)
        filter_s = list(filter_s)
        filter_lower = [ch.lower() for ch in filter_s]
        
        start= 0
        end = len(filter_lower)-1
        
        while start <=end:
            if filter_lower[start]!=filter_lower[end]:
                return False
            start+=1
            end-=1
        return True
        
​
