class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms=0
        start=sorted([x[0] for x in intervals])
        end=sorted([x[1] for x in intervals])
        j=0
        k=0
        i=0
        l=len(intervals)
        
        if not intervals:
            return 0
        while(i<l):
            if start[i]>=end[j]:
                rooms-=1
                j+=1
            rooms+=1
            i+=1
        
        return rooms
        
            
            
            
        
            
