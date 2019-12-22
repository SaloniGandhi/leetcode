class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q=[]
        visited=[]
        q.append('0000')
        visited.append('0000')
        level=0
        while(q):
            currentstate=q.pop(0)
            if currentstate==target:
                return level
            if currentstate in deadends:
                continue
            else :
                #create the two possible strings of the current state
                lock=currentstate
                for i in range(0,4):
                    changeposition=lock[i]
                    cp1=int(lock[i])+1 if int(lock[i])+1<10 else 0
                    cp2=int(lock[i])-1 if int(lock[i])-1>=0 else 9
                    s1=lock[0:i]+str(cp1)+lock[i+1:]
                    s2=lock[0:i]+str(cp2)+lock[i+1:]             
                if s1 not in visited and s1 not in deadends:
                    visited.append(s1)
                    q.append(s1)
                if s2 not in visited and s2 not in deadends:
                    visited.append(s2)
                    q.append(s2)
            level+=1
        return -1
