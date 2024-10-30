#Input: s = "()[]{}"
#Output: true
#we use a stack and everytime we encounter an opening bracket we push it to the stack. When we encounter a closing bracket, we check wheather the opening bracket
#for the current closing bracket is on top of the stack. If it is on top of the stack then we pop it out of the stack else we return False.


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i=="(" or i=="{" or i=="[" :
                stack.append(i)
            else:
                if stack == []:
                    return False
                if i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        return stack ==[]