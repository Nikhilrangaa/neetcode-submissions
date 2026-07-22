class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            bigger = -heapq.heappop(stones)
            smaller = -heapq.heappop(stones)

            if smaller < bigger:
                bigger = -(bigger - smaller)
                heapq.heappush(stones, bigger)
        
        if stones:
            return -stones[0]
        return 0
        
                
    
