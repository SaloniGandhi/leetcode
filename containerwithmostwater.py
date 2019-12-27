class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''area=0
        current=0
        if len(height)==0:
            return 0
        elif len(height)==1:
            return height[0]
        elif len(height)==2:
            return min(height)
        #keep on adding until the next element is greater than the current
        else:
            for i in range(len(height[1:])):
                if height[current]>=height[i]:
                    area+=height[current]
                else:
                    current+=1
            return area
           ''' 
        area=0
        i=0
        j=len(height)-1
        while(i<j):
            breadth=min(height[i],height[j])
            length=abs(j-i)
            area=max(area,breadth*length)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return area
