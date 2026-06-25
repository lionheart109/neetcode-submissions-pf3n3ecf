class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(0 , len(nums)-1) :
            num = nums[i]
            right = len(nums) -1 
            left = i + 1
            while left < right :
                if num + nums[left] + nums[right] < 0:
                    left += 1 
                elif num + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                     ans.add(tuple([num, nums[left], nums[right]]))
                     left += 1 
                     right -= 1
        return list(ans)