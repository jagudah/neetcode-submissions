class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        anagrams = defaultdict(list)

        for s in strs:
            alphabet = [0] * 26 #letters a-z

            for c in s:
                alphabet[ord(c) - ord('a')] += 1
            
            (anagrams[tuple(alphabet)]).append(s)

        return list(anagrams.values())