class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums)-1
        while start <= end:
            middle = (start + end)//2
            
            if target > nums[middle]:
                start = middle + 1
            elif target < nums[middle]:
                end = middle -1
            elif target == nums[middle]:
                return middle
​
        return -1
        
