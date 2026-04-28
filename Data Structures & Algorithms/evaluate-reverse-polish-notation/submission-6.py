import collections
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = collections.deque()
        for i in tokens:
            if i!="+" and i!="-" and i!="*" and i!="/":
                res.append(int(i))
            else:
                a = int(res.pop())
                b = int(res.pop())
                if i=="+":
                    res.append(a + b)
                if i=="-":
                    res.append(b-a)
                if i=="*":
                    res.append(a * b)
                if i=="/":
                    res.append(int(b/a))
        return res[-1]