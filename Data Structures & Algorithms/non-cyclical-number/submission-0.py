class Solution:
    def isHappy(self, n: int) -> bool:
        hashSet = set()
        q = deque()
        q.append(n)
        while q:
            temp = 0
            q_int = q.popleft()
            q_str = str(q_int)
            for char in q_str:
                temp += pow(int(char), 2)
            if temp == 1:
                return True
            elif temp in hashSet:
                return False
            else:
                hashSet.add(temp)
                q.append(temp)
        return False