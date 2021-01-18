class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run_sum = 0
        runningSum = [0] * len(nums)
        for i in range(len(nums)):
            run_sum = run_sum + nums[i]
            runningSum[i] = run_sum
        return runningSum
            
