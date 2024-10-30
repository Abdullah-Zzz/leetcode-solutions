class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        out = 0

        for op in operations:
            if op.lstrip('-').isdigit():
                res.append(int(op))
            elif op == '+':
                newScore = res[-1] + res[len(res)-2]
                res.append(newScore)
            elif op == 'D':
                newScore = res[-1]*2
                res.append(newScore)
            elif op == 'C':
                res.pop()
            
        for i in res:
            out += i
        return out