class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        counter=0
        for i in range(0,len(points)):
            a=points[i]
            if x==a[0] or y==a[1]:
                dist=abs(x-a[0])+abs(y-a[1])
                if counter==0:
                    nearest_dist=dist
                    index=i
                    counter+=1
                elif nearest_dist>dist:
                    nearest_dist=dist
                    index=i
        if counter==0:
            return -1
        else:
            return index
            