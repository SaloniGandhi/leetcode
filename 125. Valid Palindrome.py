from copy import *
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s=="":
            return True
        if not s:
            return False
        l=[p for p in s.lower() if p.isalnum()]
        print(l)
        l.reverse()
        if l==l[::-1]:
            return True
            
        return False
            
        
            
