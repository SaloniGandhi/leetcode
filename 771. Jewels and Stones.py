class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jdict={}
        count=0
        for item in J:
            jdict[item]=1
        for item in S:
            if item in jdict:
                count+=1
        return count
            
        
