class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def search_help(start, end, nums, target):
            
            
            if start <= end:
                middle = (start + end)//2
                if target == nums[middle]:
                    return middle
                elif target > nums[middle]:
                    return search_help(middle+1,end,nums,target)
                else:
                    return search_help(start,middle-1,nums,target)
            else:
                return -1
    
        return search_help(0,len(nums)-1, nums, target)
        
        
