class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        result1=[]
        result2=[]
        #lets push all digit logs first
        for i in (logs):
                if  i[-1].isdigit():
                    result1.append(i)
                else:
                    result2.append(i)
        print (result2)
        result2.sort(key = (lambda x: (x.split()[1:], x.split()[0])))
        final=result2+result1
        return final
