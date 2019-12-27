class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q=[]
        if not rooms:
            return
        maxi=len(rooms)
        maxj=len(rooms[0])
        #iterate over the grid look for zeroes
        for i in range(len(rooms)):
            for j in range (len(rooms[0])):
                if rooms[i][j]==0:    
                    q.append((i,j))
    #append those locations where i,j is 0
        while(q):
            level=1
            tup=q.pop(0)
            i=tup[0]
            j=tup[1]
            for ni,nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=ni<maxi and 0<=nj<maxj:
                    if rooms[ni][nj]==2147483647:
                        rooms[ni][nj]=rooms[i][j]+level
                        q.append((ni,nj))
            level+=1
        return rooms
        
      
        
