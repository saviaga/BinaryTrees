class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums_d = collections.Counter(nums)
        #order the elements by ocurrence, returns the highest
        for key in sorted(nums_d, key=nums_d.get,reverse=True):
            return key