
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-x for x in stones] #max heap
        heapq.heapify(h)
        while len(h)>1:

            heapq.heappush(h,heapq.heappop(h)-heapq.heappop(h))
     
        return -h[0]
        