class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        traversed_nums={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in traversed_nums:
                return [traversed_nums[diff],i]
            else:
                traversed_nums[nums[i]]=i
        return False
            