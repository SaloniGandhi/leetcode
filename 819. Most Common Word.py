from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace(',', ' ')
        paragraph = paragraph.replace('.', ' ')
        paragraph = paragraph.replace(';', ' ')
        paragraph = paragraph.replace('\'', ' ')
        paragraph = paragraph.replace('?', ' ')
        paragraph = paragraph.replace('!', ' ')
        paragraph = paragraph.lower()
        item = [i.strip('') for i in paragraph.split(' ') if i != '']
        res = []
        for i in item:
	        if i not in banned:
		        res.append(i)
        c = Counter(res)
        # print(c)
        return c.most_common(1)[0][0]
