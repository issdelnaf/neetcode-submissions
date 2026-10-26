class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        for n in nums:
            hmap[n]=hmap.get(n,0)+1
        newh=defaultdict(list)
        lista=[]
        for i in hmap:
            newh[hmap[i]].append(i)
        lista=sorted(newh.keys(),reverse=True)
        f=[]
        for i in range(len(lista)):
            f.extend(newh[lista[i]])
        return f[ :k]
        