#we create a hashmap and sort out every word. we store the sorted word as the key in hashmap and all of its anagrams as the value of the key using an array.
#[eat,tea,state,taste,bat,tab] , {"aet":["eat","tea"], "aestt":["state","taste"], "abt":["bat","tab"]} 

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