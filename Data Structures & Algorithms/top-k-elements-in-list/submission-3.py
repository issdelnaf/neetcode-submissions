class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        for n in nums:
            hmap[n]=hmap.get(n,0)+1
        newh=defaultdict(list)
        for i in hmap:
            newh[hmap[i]].append(i)
        a=sorted(newh.keys(),reverse=True)
        listn=[]
        for i in range(min(len(a),k)):
            listn.extend(newh[a[i]])
        return listn[:k]


        
        