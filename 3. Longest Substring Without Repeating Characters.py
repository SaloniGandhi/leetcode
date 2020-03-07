class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i_pointer=0
        j_pointer=0
        seen=set()
        maxsubstr=0
        while(j_pointer<len(s)):
            if s[j_pointer] not in seen:
                seen.add(s[j_pointer])
                j_pointer+=1
                maxsubstr=max(len(seen),maxsubstr)
            elif s[j_pointer] in seen:
                seen.remove(s[i_pointer])
                i_pointer+=1     
        return maxsubstr
