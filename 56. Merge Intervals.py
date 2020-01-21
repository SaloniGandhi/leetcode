class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort list on start times
        intervals = sorted(intervals)
        print(intervals)
        merged=[]
        if not intervals:
            return
        if len(intervals)==1:
            return intervals
        merged.append(intervals[0])
        current=merged[-1]
        for item in intervals[1:]:
            if current[1]>=item[0]:
                if merged:
                    merged.pop()
                starttime=current[0]
                endtime=max(current[1],item[1])
                time=[starttime,endtime]
                merged.append(time)
                current=merged[-1]
            else:
                merged.append(item)
                current=item      
        return merged
