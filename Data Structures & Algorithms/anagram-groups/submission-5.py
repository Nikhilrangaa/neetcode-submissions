class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_hashmap = {}

        for s in strs:
            key = tuple(sorted(s))
            if key not in sorted_hashmap:
                sorted_hashmap[key] = []
            
            sorted_hashmap[key].append(s)
        
        return list(sorted_hashmap.values())
        








        
        