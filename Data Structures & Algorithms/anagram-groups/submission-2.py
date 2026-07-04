class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            letters = [0] * 26

            for c in word:
                letters[ord(c) - ord('a')] += 1

            result[tuple(letters)].append(word)
        
        return list(result.values())