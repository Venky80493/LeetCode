class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==k:
            return nums
        nums_dict={}
        res=[]
        freq=[[] for i in range(len(nums)+1)]
        for num in nums:
            nums_dict[num]=nums_dict.get(num,0)+1
        for n,c in nums_dict.items():
            freq[c].append(n)
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
        