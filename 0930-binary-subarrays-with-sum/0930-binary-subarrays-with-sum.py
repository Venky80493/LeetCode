class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res=0
        currSum=0
        count={0:1}
        for n in nums:
            currSum+=n
            diff=currSum-goal
            res+=count.get(diff,0)
            count[currSum]=1+count.get(currSum,0)
        return res
            