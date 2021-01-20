class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_dic = {}
        new_words = []
        #1. create a dictionary with the positions of the alien dictionary
        
        for pos in range(0,len(order)):
            alien_dic[order[pos]] = pos
        
        #2. Transform the list of words into its index in new order.
        #words = ["hello","leetcode"] -> [[0, 6, 1, 1, 14], [1, 6, 6, 19, 4, 14, 5, 6]]
        for word in words:
            new = []
            for char in word:
                new.append(alien_dic[char])
            new_words.append(new)
       
        #zip(words, words[1:]) here will combine first element(words[0]) in words with
        #words[1], so we can compare current element with next element: 0->1, 1->2
      
        for w1,w2 in zip(new_words,new_words[1:]): 
            #print(w1,w2)
            
            #words = ["apple","app"],"apple" > "app", because 'l' > '∅',hence False
            #null is less than anything
            if w1 > w2:
                return False
        return True
        
        
        
        
        
                
        
        
​
