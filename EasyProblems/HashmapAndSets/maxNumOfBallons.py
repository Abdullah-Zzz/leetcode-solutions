#we find the number of times every char is repeated in the text using a dict {"b":1,"a":1,"l":2}. after that we check whether the char in "balloon" exists 
#in the dixt. If they exist we then check whether they are atleast repeated or used as many times as required . to create one instance of "balloon" we check
#whether 'b','a','n' are repeated one time and 'l' and o are repeated two times if this is the case we update that the text consists one instance of balloon
#then we update the count of each char in the dict and check for values again


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        charCount ={}
        out=0

        for ltr in text:
            if ltr in charCount:
                charCount[ltr] +=1
            else:
                charCount[ltr] = 1
        
        for i in text:
            if 'b' not in charCount or 'a' not in charCount or 'l' not in charCount or 'o' not in charCount or 'n' not in charCount:
                return out
            if charCount['b'] >=1 and charCount['a'] >=1 and charCount['l'] >=2 and charCount['o'] >=2 and charCount['n'] >=1:
                out +=1
                charCount['b'] -=1
                charCount['a'] -=1
                charCount['l'] -=2
                charCount['o'] -=2
                charCount['n'] -=1
            else:
                return out
