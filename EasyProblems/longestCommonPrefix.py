#for every letter in the first string we will check wheather the letter at the same position in the other strings is the same. we will first check if the 
#first letter of the first string is the same as the first letter of the second string then we will check if the first letter of the third string is the same
#as the first letter of the first string and so on till the last string then we will go towards the second letter of the first string and do the same ONLY IF 
#all the first letters of the string are the same.
  

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            res = ""
            for i in range(len(strs[0])):
                for s in strs:
                    if i==len(s) or s[i] != strs[0][i]:
                        return res 
                res += strs[0][i]
            return res 
