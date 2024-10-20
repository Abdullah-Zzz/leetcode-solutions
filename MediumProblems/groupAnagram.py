class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        hashmap = {}
        for s in strs:
            sortedWord = sorted(s)
            key = ''.join(sortedWord)
            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]
        for key in hashmap:
            out.append(hashmap[key])
        return out