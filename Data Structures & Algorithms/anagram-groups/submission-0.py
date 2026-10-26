class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            a=str(sorted(s))
            hmap[a].append(s)
        return list(hmap.values())
        