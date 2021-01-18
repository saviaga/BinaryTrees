class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        letters = dict()
        check = list(A[0])
        
        for elem in A:
            intersection = []
            for ch in elem:                
                if ch in check:
                    intersection.append(ch)
                    check.remove(ch)
            check = intersection
        return intersection
            
                    
        
        
                
        
        
        
