class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #find minimum of all strs
        #iterate over strs and check if every corresponsing letter is present if yes then append to empty string
        result=""
        if len(strs)==1:
            return strs[0]
        if not strs:
            return ""
        minlenstr=min(strs, key=len)        
        for i in range (len(minlenstr)):
            currentchar=strs[0][i]
            for s in strs[1:]:
                if currentchar!=s[i]:
                    return result
            result+=currentchar
        print (result)
        return result
