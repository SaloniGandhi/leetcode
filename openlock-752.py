class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q=[]
        visited=[]
        q.append('0000')
        visited.append('0000')
        while(q):
            level=0
            currentstate=q.pop(0)
            if currentstate==target:
                return level
            if currentstate in deadends:
                continue
            elif currentstate not in deadends:
                #create the two possible strings of the current state
                lock=currentstate
                for i in range(0,4):
                    changeposition=lock[i]
                    if changeposition=='9':
                        changeposition='0'
                    else:
                        changepsoition1=changeposition-'0'+'1'
                        changeposition2=changeposition-'0'-'1'
                    s1=lock[0:i]+changeposition1+lock[i+1:]
                    s2=lock[0:i]+changeposition2+lock[i+1:]             
                if s1 not in visited and s1 not in deadends:
                    visited.append(s1)
                    q.append(s1)
                if s2 not in visited and s2 not in deadends:
                    visited.append(s2)
                    q.append(s2)
                
                
                
            level+=1
        return level
