#we go through the list tokens and we check if the current value is an operator. If it is not an operator (An integer) we append it into the stack.If it is an
#operator we take the last two elements  in the stack and perform the operation (+,-,*,/) on them. we pop the last two elements and store the result in their 
#place

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for num in tokens:
            if num == '+':
                SUM = stack[-2] + stack[-1]
                stack.pop()
                stack[-1] = SUM
            elif num == '-':
                diff = stack[-2] - stack[-1]
                stack.pop()
                stack[-1] = diff
            elif num == '*':
                mul = stack[-2] * stack[-1]
                stack.pop()
                stack[-1] = mul
            elif num == '/':
                div = int(stack[-2] / stack[-1])
                stack.pop()
                stack[-1] = div
            else:
                stack.append(int(num))
        return stack[0]