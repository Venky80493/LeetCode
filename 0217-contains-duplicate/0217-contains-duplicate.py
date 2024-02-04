class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        int_count={}
        for i in nums:
            if i in int_count.keys():
                return True
            else:
                int_count[i]=1