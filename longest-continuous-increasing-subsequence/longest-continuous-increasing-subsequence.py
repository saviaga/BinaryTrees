class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1

        start,ans = 0,0
         
        for i in range(len(nums)):
            
            if i and nums[i-1] >= nums[i] : 
                start = i
            ans = max(ans, i - start + 1)
        return ans
        

        