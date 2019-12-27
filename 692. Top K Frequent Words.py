import collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = collections.Counter(sorted(words))
        return [i[0] for i in c.most_common(k)]
