#same solution and explanation as valid anagram prob

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charCount = {}
        for ltr in magazine:
            if ltr in charCount:
                charCount[ltr] +=1
            else:
                charCount[ltr] = 1
        for ltr in ransomNote:
            if ltr in charCount and charCount[ltr] > 0:
                charCount[ltr] -=1
            else:
                return False
        return True

