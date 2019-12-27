class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words=sorted(words,key=len)
        licensePlate=licensePlate.lower()
        s=""
        for letter in licensePlate:
            if letter.isalpha():
                s+=letter
        for word in words:
            temp=s
            for char in word:
                if char in temp:
                    #removing first instance of the letter which occours
                    temp=temp.replace(char,'',1)
        
            if len(temp)==0:
                return word
                    
                
        
