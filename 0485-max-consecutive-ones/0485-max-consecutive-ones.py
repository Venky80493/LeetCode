class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count,count=0,0
        for i in nums:
            if i!=0:
                count+=1
            else:
                count=0
            max_count=max(max_count,count)
        return max_count
            