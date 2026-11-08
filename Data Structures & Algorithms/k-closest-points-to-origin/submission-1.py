class Solution:
    def getDistances(self, x, y):
        dist = math.sqrt(pow(x,2) + pow(y, 2))
        return [dist, [x,y]]
        
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances, res = [], []
        for x, y in points:
            distances.append(self.getDistances(x, y))
        heapq.heapify(distances)
        while k > 0:
            dist, loc = heapq.heappop(distances)
            res.append([loc[0], loc[1]])
            k -= 1
        return res