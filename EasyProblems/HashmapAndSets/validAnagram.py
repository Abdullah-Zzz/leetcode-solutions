#anagram are the words which contain the same letters but the positions are changed for example state and taste are anagram. by this we can say that an anagram
#contains the same number of char and the same char as it anagram. we kept count of the characters in s and moved through the letters in t . As we move through
#them we check whether they exist in t. 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charCount = {}

        for ltr in s:
            if ltr in charCount:
                charCount[ltr] +=1
            else:
                charCount[ltr] = 1

        for ltr in t:
            if ltr in charCount and charCount[ltr] > 0:
                charCount[ltr] -=1
            else:
                return False
        return True     