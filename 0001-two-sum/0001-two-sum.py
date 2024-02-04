class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        traversed_nums={}
        for i in range(len(nums)):
            if target-nums[i] in traversed_nums.keys():
                return [traversed_nums[target-nums[i]],i]
            else:
                traversed_nums[nums[i]]=i
        return False
            