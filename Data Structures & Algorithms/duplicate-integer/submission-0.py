class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        while nums:
            fnd = nums.pop()
            for num in reversed(nums):
                if fnd == num:
                    return True
                    break
        return False

