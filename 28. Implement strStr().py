class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        '''
        n=len(needle)
        for i in range(len(haystack)-n+1):
            if haystack[i]==needle[0]:
                if needle==haystack[i:i+n]:
                    return i
            
        return -1
        '''
        
        i=0
        j=0
        while i<len(needle) and j<len(haystack):
            if needle[i]!=haystack[j]:
                j=j-i+1
                i=0
            elif needle[i]==haystack[j]:
                i+=1
                j+=1
                continue
        if len(needle)==i:
            return j-i
        return -1
    
    
    
