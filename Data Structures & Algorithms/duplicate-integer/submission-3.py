class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        #sort the array
        #nums.sort()
        #for i in range(n-1):
        #    if nums[i] == nums[i+1]:
        #        return True
        
        #hash map / dict
        hmap = {}
        for i in range(n):
            hmap[nums[i]] = hmap.get(nums[i], 0) + 1
            if hmap[nums[i]] >= 2:
                return True


        
        return False