class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        #sort the array
        nums.sort()
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                return True
        
        return False