class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        best = {}
        for i , value in enumerate(nums):
            best.update({value:i})
        i=0
        for num in nums:
            if best.get(target - num,-1) != -1 and i != best.get(target - num):
                return([i,best.get(target - num)])
            i+=1