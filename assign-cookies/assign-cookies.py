class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        children =0
        pg=0
        ps=0
        while ps<len(s) and pg<len(g):
            
            if s[ps]>=g[pg]:
                ps+=1
                pg+=1
                children+=1                
            else:
                
                ps+=1
            
        return children            
        

