class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        buckets = []
        output = []

        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
        
        buckets = [[] for i in range(len(nums) + 1)]

        for n in hashmap:
            buckets[hashmap[n]].append(n)
        

        for i in range(len(nums), -1, -1):
            for n in buckets[i]:
                output.append(n)

            if len(output) == k:
                return output




        