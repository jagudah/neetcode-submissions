class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        distances = []
        for i in range(len(points)):
            distance = math.sqrt(pow(points[i][0], 2) + pow(points[i][-1], 2))
            distances.append([distance, i])
        heapq.heapify(distances)
        while k > 0:
            distance, index = heapq.heappop(distances)
            result.append(points[index])
            k -= 1
        return result