class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n= len(nums)
        # for i,j in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        #             continue
        #nums.sort()
        # i=0
        # j=n-1
        # while i<j:
        #     if nums[i]+nums[j]==target:
        #         return [i,j]
        #     elif nums[i]+nums[j]>target:
        #         j=j-1
        #     elif nums[i]+nums[j]<target:
        #         i=i+1
        # return False
        A=[]
        for i,num in enumerate(nums):
            A.append([num,i])
        A.sort()
        i=0
        j=n-1
        while i<j:
            if A[i][0]+A[j][0]==target:
                return [min([A[i][1],A[j][1]]),max([A[i][1],A[j][1]])]
            elif A[i][0]+A[j][0]>target:
                j=j-1
            elif A[i][0]+A[j][0]<target:
                i=i+1
        return []


