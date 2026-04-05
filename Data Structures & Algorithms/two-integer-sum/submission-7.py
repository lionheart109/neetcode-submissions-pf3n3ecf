class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        best = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if best.get(val,-1) != -1:
                return([best.get(val),i])
            best.update({nums[i]:i})