# s = ace , t = aghcije; make two counters or indexes for s and t ls and lt , check wheather t at lt index t[lt] matches s at ls index s[ls] , if it does increment
#both of the indexes if not only increment the index for t. we will keep on moving through t while checking for a match for a letter in s if a match is found 
# we will start checking for the next letter of s in t from where we left off in t or from where we found the previous match  in t and we will keep on checking 
#untill the index for either t or s reaches the len of their respective string.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls = 0
        lt = 0
        while lt < len(t) and ls < len(s):
            if s[ls] == t[lt]:
                ls +=1
                lt +=1
            else:
                lt+=1 
        return ls == len(s)


