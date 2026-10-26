class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        i=0
        j=n-1
        water=0
        while i<j:
            width=j-i
            height=min(heights[i],heights[j])
            if water<width*height:
                water=width*height
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return water
            

        