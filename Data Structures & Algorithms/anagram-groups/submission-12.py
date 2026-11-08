class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            sortedWord = ''.join(sorted(word))
            res[sortedWord].append(word)
        return list(res.values())