class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letterMap = defaultdict(list)
        for word in strs:
            letters = [0] * 26

            for char in word:
                letters[ord(char) - ord('a')] += 1
            
            letterMap[tuple(letters)].append(word)
        
        return list(letterMap.values())