class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1.0
        res = 1.0
        dummy_n = abs(n)
        while dummy_n > 1:
            if dummy_n%2:
                res*=x
                dummy_n-=1
            else:
                x*=x
                dummy_n//=2
        res*=x
        if n<0: res = 1/res
        return res
        