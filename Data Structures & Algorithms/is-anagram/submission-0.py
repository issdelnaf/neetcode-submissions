class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap={}
        for i in s:
            hmap[i]=hmap.get(i,0)+1
        for j in t:
            hmap[j]=hmap.get(j,0)-1
        for i in hmap:
            if hmap[i]<0 or hmap[i]>0:
                return False
        return True
        