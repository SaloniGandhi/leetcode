class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        i=0
        letterdict={}
        for letter in order:
            letterdict[letter]=i
            i+=1
        #first letter diif
        p=0
        for j in range (len(words)-1):
            if letterdict.get(words[j][0])>letterdict.get(words[j+1][0]):
                return False
            #first letter matches,check subsequent letter
            if letterdict.get(words[j][0])==letterdict.get(words[j+1][0]):
                if self.helper(words[j],words[j+1],letterdict)==False:
                    return False
            
        return True
    #helper checks similarity of 2 words
    def helper(self,word1,word2,letterdict):
        loopcount=min(len(word1),len(word2))
        for i in range (loopcount-1):
            if word1[i]==word2[i]:
                continue
            else:
                if letterdict.get(word1[i])<letterdict.get(word2[i]):
                    return True
        return False
        
        
         
        
