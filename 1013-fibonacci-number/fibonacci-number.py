class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        prev_1 = 0
        prev_2 = 1
        for i in range(2,n+1):
            result = prev_1 + prev_2
            prev_1 = prev_2
            prev_2 = result
        return result
            
