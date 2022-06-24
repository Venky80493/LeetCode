class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        nearest_dist=10000000
        counter=0
        for i in range(len(points)):
            a=points[i]
            if x==a[0] or y==a[1]:
                dist=abs(x-a[0])+abs(y-a[1])
                if nearest_dist>dist:
                    nearest_dist=dist
                    counter+=1
                    index=i
        if counter>0:
            return index
        else:
            return -1