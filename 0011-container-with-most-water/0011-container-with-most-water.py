class Solution:
    def maxArea(self, height: List[int]) -> int:
        self.height=height
        area=0
        l,r=0,len(height)-1
        while l<r:
            if min(height[l],height[r]) * (r-l)>area:
                area=min(height[l],height[r]) * (r-l)
            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
        return area
            
        