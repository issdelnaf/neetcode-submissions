class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        blist=[]
        for k in range(n-2):
            target=-nums[k]
            i=k+1
            j=n-1
            while i<j:
                if nums[i]+nums[j]==target:
                    l=[nums[k],nums[i],nums[j]]
                    if l not in blist:
                        blist.append(l)
                    i+=1
                    j-=1
                elif nums[i]+nums[j]>target:
                    j-=1
                elif nums[i]+nums[j]<target:
                    i+=1
        return blist
        

        