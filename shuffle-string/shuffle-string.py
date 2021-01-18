class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        l_s = list(s)
        n_s = [0] * len(s)
        
        for i in range(len(indices)):
            n_s[indices[i]] = l_s[i]
        
        return ''.join(n_s)
