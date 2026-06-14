from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        k_values = []
        
        for number in nums:
            if number not in count:
                count[number] = 1
            else:
                count[number] += 1
        sorted_keys = sorted(count, key=count.get, reverse=True)
        top_k = sorted_keys[:k]
        return top_k
        



        


