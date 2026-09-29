class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for word in strs:
            letters = [0] * 26
            for c in word:
                letters[ord(c) - ord('a')] += 1
            mp[tuple(letters)].append(word)
        return list(mp.values())