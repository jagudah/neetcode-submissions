class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            alphabet = [0] * 26 # For letters a...z

            for c in s:
                alphabet[ord(c) - ord('a')] += 1
            res[tuple(alphabet)].append(s)
        return list(res.values())
