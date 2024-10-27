# we go through the list and store all the letters of the sentence in a variable.Then we use a Two pointers approach to check if it is a palindrome.
#Input: s = "A man, a plan, a canal: Panama"
#Output: true
#Explanation: "amanaplanacanalpanama" is a palindrome.  
#"amanaplanacanalpanama"
# i                   j     we make two pointers.We increment i and decrement j until they meet at the center. As we increment and decrement these pointers
#we also check if the letter or character at index i is equal to the letter at index j. 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True

        res = ""
        for ltr in s:
            if ltr ==" ":
                continue
            elif ltr.isalnum():
                res = res+ltr.lower()

        i = 0
        j = len(res)-1
        while i < j:
            if res[i] == res[j]:
                i+=1
                j-=1
            else:
                return False 
        return True