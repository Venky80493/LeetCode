class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums=sorted(nums,reverse=True)
        i=0
        while i>=0 and i+2<=(len(nums)-1):
            print(nums[i])
            if nums[i+2]+nums[i+1]>nums[i]:
                return nums[i]+nums[i+1]+nums[i+2]
            i=i+1
        return 0