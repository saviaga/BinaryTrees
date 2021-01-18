from itertools import zip_longest
​
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
​
        for char1, char2 in zip_longest(self.string_iter(word1), self.string_iter(word2)):
                if char1!=char2:
                    return False
        return True
​
​
    def string_iter(self,words:List[str])->chr:
                for word in words:
                    for char in word:
                        yield char
​
