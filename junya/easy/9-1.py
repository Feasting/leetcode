class Solution:
    def reverse(self, x: int) -> int:
        if x is 0:
            return 0
        ret = str(x)[::-1]
        
        while ret[0] is "0":
            ret = ret[1:]
        print(ret[-1])
        if ret[-1] is "-":
            ret = "-" + ret[:-1]
        top = 2**31 - 1
        bot = -1 * 2**31
        ret = float(ret)
        if ret <= top and ret >= bot:
            return int(ret)
        else:
            return 0

# https://leetcode.com/problems/reverse-integer/
