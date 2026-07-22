class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #initializing the nums list and k value
        self.nums = nums
        self.k = k
        #turning nums ianto a min heap
        heapq.heapify(nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]



        
