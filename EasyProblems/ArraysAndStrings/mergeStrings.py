class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedString = ""

        #finding the len of the smaller strings so we know how many times to run the loop
        smallerString = len(word1) if len(word1) < len(word2) else len(word2)

        #running the loop and appending one letter of the first word then one letter of the second word 
        for i in range(0,smallerString):
            mergedString += word1[i] 
            mergedString += word2[i]

        #the loop will run as many times as the len of the smaller word, eg: word1 = "red", word2 = "blue". the loop will run three times
        #the question asked to append the remaining letters at the end of the merged string 
        #these conditions are used to check wheather there are letters left and if there are then in which word 
        if len(word1) > len(word2):
            #if there are letters left, we append all of the letters at the end of the merged string  
            mergedString += word1[smallerString:]
        elif len(word2) > len(word1):
            mergedString += word2[smallerString:]
        
        return mergedString
