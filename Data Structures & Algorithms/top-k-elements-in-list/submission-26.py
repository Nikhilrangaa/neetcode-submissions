class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            if n in results:
                results[n] += 1
            else:
                results[n] = 1
        
        for n, count in results.items():
            freq[count].append(n)
        
        answer = []

        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                answer.append(n)

                if len(answer) == k:
                    return answer
                
        

            
            


            

            

        