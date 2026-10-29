class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []
        def backtrack(i, cur, total):
            if total == target:
                self.res.append(cur.copy())
                return
            if i == len(candidates):
                return
            for j in range(i, len(candidates)):
                if (j > i and candidates[j] == candidates[j-1]) or total + candidates[j] > target:
                    continue
                cur.append(candidates[j])
                backtrack(j+1, cur, total+candidates[j])
                cur.pop()
        backtrack(0, [], 0)
        return self.res