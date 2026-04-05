class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        best = dict(enumerate(nums))
        while i < len(nums):
            find = target - nums[i]
            for key , value in best.items():
                if value == find and key != i:
                    return [i , key]
            i+=1