class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_strs=defaultdict(list)
        for str in strs:
            str_sorted=''.join(sorted(str))
            map_strs[str_sorted].append(str)
        return map_strs.values()
            