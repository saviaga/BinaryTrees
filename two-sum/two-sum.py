class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        dict_nums={}
        
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in dict_nums:
                dict_nums[nums[i]] = i
            else:
                return i, dict_nums[complement]
        
        return -1,-1
        
