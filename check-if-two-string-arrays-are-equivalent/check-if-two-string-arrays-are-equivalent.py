class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        concat1 = ''
        concat2 = ''
        for elem in word1:
            concat1 = concat1+elem
        
        for elem in word2:
            concat2 = concat2+elem 
        return concat1 == concat2
