class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [(p,s) for p,s in zip(position, speed)]
        pos_speed = sorted(pos_speed, reverse=True)
        res = []
        for i in pos_speed:
            res.append((target - i[0])/i[1])
            if len(res)>=2 and res[-1] <= res[-2]:
                res.pop()
        return len(res)