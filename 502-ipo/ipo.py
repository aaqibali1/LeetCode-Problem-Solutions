import heapq
from typing import List

class T:
    def __init__(self, pro, cap):
        self.pro = pro
        self.cap = cap
        
    def __lt__(self, other):
        return self.cap < other.cap

class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        minHeap = []
        maxHeap = []

        for i in range(len(Capital)):
            heapq.heappush(minHeap, T(Profits[i], Capital[i]))

        while k > 0:
            while minHeap and minHeap[0].cap <= W:
                t = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, (-t.pro, t.cap))
            if not maxHeap:
                break
            p, c = heapq.heappop(maxHeap)
            W -= p
            k -= 1

        return W