import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]: # type: ignore
        heap = []

        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(heap, (-dist, [x,y]))

            if len(heap) > k:
                heapq.heappop(heap)
            

        return [p for dist, p in heap]